from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import mysql.connector
import os
import socket
from datetime import date, datetime



app = Flask(__name__)

# Uploads folder setup
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database configuration
db_config = {
    "host": "rpgmoose.mysql.pythonanywhere-services.com",
    "port": 3306,
    "user": "rpgmoose",
    "password": "!NPstar123!",
    "database": "rpgmoose$RECORDS"
}

# Debug print for DB config (excluding password)
print("Connecting with DB config:")
print({k: v for k, v in db_config.items() if k != "password"})

# Establish DB connection
try:
    db = mysql.connector.connect(**db_config)
    print("Successfully connected to database.")
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
    exit(1)

# Homepage route: list all students
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    cursor.close()
    return render_template('homepage.html', students=students)

# View a single student's attendance
@app.route('/attendance/<int:r_number>')
def view_attendance(r_number):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT Attendance.date, Attendance.attendance_status
        FROM Attendance
        WHERE Attendance.r_number = %s
    """, (r_number,))
    attendance_records = cursor.fetchall()

    cursor.execute("SELECT first_name, last_name FROM Students WHERE r_number = %s", (r_number,))
    student = cursor.fetchone()

    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    cursor.close()

    return render_template(
        'homepage.html',
        students=students,
        selected_student=student,
        attendance_records=attendance_records
    )

# Upload route (e.g., for images)
@app.route('/upload', methods=['POST'])
def upload():
    image = request.files.get('image')

    if image and image.filename != '':
        filename = secure_filename(image.filename)
        image_path = os.path.join(UPLOAD_FOLDER, filename)
        image.save(image_path)

        # (Optional) Insert image processing here
        return redirect(url_for('index'))
    else:
        return "No image uploaded", 400

# Mark attendance route
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    r_number = request.form['r_number']
    course_id = request.form['course_id']
    instructor_id = request.form['instructor_id']
    attendance_status = request.form['attendance_status']
    date = request.form['date']
    time = request.form['time']

    cursor = db.cursor()
    try:
        cursor.execute("""
            INSERT INTO Attendance (r_number, course_id, instructor_id, attendance_status, date, time)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (r_number, course_id, instructor_id, attendance_status, date, time))
        db.commit()
    except mysql.connector.Error as err:
        print("Error inserting attendance:", err)
    finally:
        cursor.close()

    return redirect(url_for('index'))

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    data = request.get_json()
    present = data.get('present', [])
    absent = data.get('absent', [])

    course_id = 4366  # or dynamically set
    instructor_id = 0  # adjust accordingly
    today = date.today()
    now = datetime.now().strftime('%H:%M:%S')

    cursor = db.cursor()

    try:
        # Handle PRESENT students
        for r_number in present:
            cursor.execute("""
                UPDATE Attendance
                SET attendance_status = TRUE, date = %s, time = %s
                WHERE r_number = %s AND course_id = %s AND instructor_id = %s AND date = %s
            """, (today, now, r_number, course_id, instructor_id, today))

            if cursor.rowcount == 0:
                cursor.execute("""
                    INSERT INTO Attendance (r_number, course_id, instructor_id, attendance_status, date, time)
                    VALUES (%s, %s, %s, TRUE, %s, %s)
                """, (r_number, course_id, instructor_id, today, now))

        # Handle ABSENT students
        for r_number in absent:
            cursor.execute("""
                UPDATE Attendance
                SET attendance_status = FALSE, date = %s, time = %s
                WHERE r_number = %s AND course_id = %s AND instructor_id = %s AND date = %s
            """, (today, now, r_number, course_id, instructor_id, today))

            if cursor.rowcount == 0:
                cursor.execute("""
                    INSERT INTO Attendance (r_number, course_id, instructor_id, attendance_status, date, time)
                    VALUES (%s, %s, %s, FALSE, %s, %s)
                """, (r_number, course_id, instructor_id, today, now))

        db.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        print("Error submitting attendance:", e)
        db.rollback()
        return jsonify({"status": "error", "message": str(e)})
    finally:
        cursor.close()



# Run app on available port
if __name__ == "__main__":
    port = 5001
    while True:
        try:
            app.run(debug=True, port=port)
            break
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"Port {port} is in use. Trying next port...")
                port += 1
            else:
                raise
