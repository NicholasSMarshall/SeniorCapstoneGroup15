from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="!NPstar123!",
    database="RECORDS"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    return render_template('homepage.html', students=students)

@app.route('/attendance/<int:r_number>')
def view_attendance(r_number):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT Attendance.date, Attendance.attendance_status
        FROM Attendance
        WHERE Attendance.r_number = %s
        """, (r_number,))
    attendance_records = cursor.fetchall()

    # Get student name
    cursor.execute("SELECT first_name FROM Students WHERE r_number = %s", (r_number,))
    student = cursor.fetchone()

    return render_template('homepage.html', students=[], selected_student=student, attendance_records=attendance_records)

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
        cursor.execute(
            "INSERT INTO Attendance (r_number, course_id, instructor_id, attendance_status, date, time) VALUES (%s, %s, %s, %s, %s, %s)",
            (r_number, course_id, instructor_id, attendance_status, date, time)
        )
        db.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        cursor.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
