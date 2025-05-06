#!C:/Python39/python.exe
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import cv2
from deepface import DeepFace
from ultralytics import YOLO
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DATABASE_FOLDER'] = 'database'
app.config['RECOGNIZED_FACES'] = 'recognized_faces'
app.config['ATTENDANCE_FOLDER'] = 'static/attendance'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DATABASE_FOLDER'], exist_ok=True)
os.makedirs(app.config['RECOGNIZED_FACES'], exist_ok=True)
os.makedirs(app.config['ATTENDANCE_FOLDER'], exist_ok=True)

# Initialize models
face_model = YOLO('yolov8n-face.pt')

# Global attendance storage
attendance_records = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def load_student_list():
    try:
        df = pd.read_excel('students.xlsx', engine='openpyxl')
        return [str(name).strip() for name in df['Student Name'].dropna().tolist()]
    except Exception as e:
        print(f"Error loading student list: {str(e)}")
        return []

def match_student_name(recognized_name, student_list):
    recognized_clean = recognized_name.strip().upper()
    for student in student_list:
        if student.strip().upper() == recognized_clean:
            return student
    return None

def process_image_for_attendance(image_path):
    image = cv2.imread(image_path)
    results = face_model(image, conf=0.1)
    recognized_faces = []
    student_list = load_student_list()
    
    # Create unrecognized_faces folder if it doesn't exist
    unrecognized_folder = 'unrecognized_faces'
    os.makedirs(unrecognized_folder, exist_ok=True)
    
    for idx, result in enumerate(results[0].boxes):
        x1, y1, x2, y2 = map(int, result.xyxy[0].tolist())
        face_image = image[y1:y2, x1:x2]
        
        temp_face_path = os.path.join(app.config['RECOGNIZED_FACES'], f"temp_face_{idx}.jpg")
        cv2.imwrite(temp_face_path, face_image)
        
        identity = "Unknown"
        confidence = 0
        recognized = False
        
        try:
            recognition_result = DeepFace.find(
                img_path=temp_face_path, 
                db_path=app.config['DATABASE_FOLDER'],
                enforce_detection=False,
                threshold=0.1,
                silent=True,
                model_name='Facenet'
            )
            
            if recognition_result and len(recognition_result[0]) > 0:
                best_match = recognition_result[0].iloc[0]
                identity_path = best_match['identity']
                confidence = 1 - best_match['distance']
                
                if confidence > 0.6:
                    recognized_name = os.path.splitext(os.path.basename(identity_path))[0]
                    matched_name = match_student_name(recognized_name, student_list)
                    
                    if matched_name:
                        identity = matched_name
                        recognized = True
                        # Update attendance records
                        today = datetime.now().strftime("%Y-%m-%d")
                        if today not in attendance_records:
                            attendance_records[today] = []
                        if identity not in attendance_records[today]:
                            attendance_records[today].append(identity)
                        
                        # Save to recognized_faces folder
                        file_name = f"{identity.replace(' ', '_')}_{idx}.jpg"
                        file_path = os.path.join(app.config['RECOGNIZED_FACES'], file_name)
                        cv2.imwrite(file_path, face_image)
        
        except Exception as e:
            print(f"Error processing face {idx}: {str(e)}")
        
        # If not recognized, save to unrecognized_faces folder
        if not recognized:
            file_name = f"unrecognized_{idx}.jpg"
            file_path = os.path.join(unrecognized_folder, file_name)
            cv2.imwrite(file_path, face_image)
        
        color = (0, 255, 0) if recognized else (0, 0, 255)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        label = f"{identity} ({confidence:.2f})" if identity != "Unknown" else identity
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        recognized_faces.append({
            'name': identity,
            'confidence': confidence,
            'matched_name': identity if identity != "Unknown" else None
        })
        
        # Remove temporary file
        if os.path.exists(temp_face_path):
            os.remove(temp_face_path)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"attendance_{timestamp}.jpg"
    output_path = os.path.join(app.config['ATTENDANCE_FOLDER'], output_filename)
    cv2.imwrite(output_path, image)
    
    return recognized_faces, output_filename

def save_attendance_to_excel(export=False):
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        master_filename = "attendancesheet.xlsx"
        student_list = load_student_list()
        present_students = attendance_records.get(today, [])
        
        # Create a set of all known students from database and attendance records
        all_known_students = set(student_list)
        
        # Check for any students in attendance records that aren't in student_list
        for date, students in attendance_records.items():
            all_known_students.update(students)
        
        # Convert back to list for consistent ordering
        all_students = sorted(all_known_students)
        
        # Create attendance status mapping for all known students
        attendance_status = {student: 'Present' if student in present_students else 'Absent' 
                          for student in all_students}

        # Try to load existing sheet
        if os.path.exists(master_filename):
            df = pd.read_excel(master_filename, engine='openpyxl', dtype=str)
            df.columns = df.columns.astype(str)
            
            # Get existing students from the sheet
            existing_students = set(df['Name/RNumber'].tolist())
            
            # Find any new students that need to be added
            new_students = all_known_students - existing_students
            
            # Create DataFrame for new students
            if new_students:
                new_rows = pd.DataFrame({'Name/RNumber': list(new_students)})
                # Set all previous dates as 'Absent' for new students
                for col in df.columns[1:]:
                    new_rows[col] = 'Absent'
                # Concatenate with existing data
                df = pd.concat([df, new_rows], ignore_index=True)
            
            # Update or add today's column
            df[today] = df['Name/RNumber'].map(attendance_status).fillna('Absent')
            
            # Reorder columns chronologically
            date_columns = sorted([col for col in df.columns if col != 'Name/RNumber'], 
                                key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
            df = df[['Name/RNumber'] + date_columns]
        else:
            # Create new DataFrame with all known students
            df = pd.DataFrame({
                'Name/RNumber': all_students,
                today: [attendance_status[student] for student in all_students]
            }, dtype=str)

        try:
            # Try using xlsxwriter first for better formatting
            with pd.ExcelWriter(master_filename, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                text_format = workbook.add_format({'num_format': '@'})
                for col_num, col_name in enumerate(df.columns):
                    if col_name != 'Name/RNumber':
                        worksheet.set_column(col_num, col_num, None, text_format)
        except ImportError:
            # Fallback to openpyxl if xlsxwriter not available
            with pd.ExcelWriter(master_filename, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)

        if export:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_filename = f"attendance_export_{timestamp}.xlsx"
            
            try:
                with pd.ExcelWriter(export_filename, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False)
                    workbook = writer.book
                    worksheet = writer.sheets['Sheet1']
                    text_format = workbook.add_format({'num_format': '@'})
                    for col_num, col_name in enumerate(df.columns):
                        if col_name != 'Name/RNumber':
                            worksheet.set_column(col_num, col_num, None, text_format)
            except ImportError:
                with pd.ExcelWriter(export_filename, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
            
            return export_filename
        
        return master_filename
    
    except Exception as e:
        print(f"Error saving attendance: {str(e)}")
        return None


@app.route('/')
def index():
    student_list = load_student_list()
    today = datetime.now().strftime("%Y-%m-%d")
    present_students = attendance_records.get(today, [])
    return render_template('homepage.html', 
                         students=student_list,
                         present_students=present_students,
                         current_date=today)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        
        recognized_faces, output_filename = process_image_for_attendance(upload_path)
        matched_students = [face['matched_name'] for face in recognized_faces if face['matched_name']]
        
        return render_template(
            'homepage.html',
            students=load_student_list(),
            recognition_results=recognized_faces,
            processed_image=output_filename,
            present_students=attendance_records.get(datetime.now().strftime("%Y-%m-%d"), []),
            show_results=True,
            current_date=datetime.now().strftime('%Y-%m-%d')
        )
    
    return redirect(url_for('index'))

@app.route('/submit_manual_attendance', methods=['POST'])
def submit_manual_attendance():
    data = request.get_json()
    manual_attendance = data.get('present', [])
    
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in attendance_records:
        attendance_records[today] = []
    
    for student in manual_attendance:
        if student not in attendance_records[today]:
            attendance_records[today].append(student)
    
    return jsonify({
        "status": "success",
        "message": f"Manual attendance recorded for {len(manual_attendance)} students"
    })


@app.route('/export_attendance', methods=['GET'])
def export_attendance():
    try:
        # Clean up old exports (keep only last 5 exports)
        export_files = sorted([f for f in os.listdir('.') 
                             if f.startswith("attendance_export_") 
                             and f.endswith(".xlsx")])
        for old_file in export_files[:-5]:  # Keep last 5 exports
            os.remove(old_file)
            
        filename = save_attendance_to_excel(export=True)
        if filename:
            return send_from_directory(
                '.', 
                filename, 
                as_attachment=True,
                mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        return "Error generating attendance report", 500
    except Exception as e:
        print(f"Export error: {str(e)}")
        return "Error generating report", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')