from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="NPstar123",
    database="RECORDS"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    return render_template('homepage.html', records=records)

if __name__ == "__main__":
    app.run(debug=True)
