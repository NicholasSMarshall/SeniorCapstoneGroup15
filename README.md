# Senior Capstone Website

This repository contains the full implementation and supporting files for our Senior Capstone Project. The project centers around a facial recognition system integrated with a lightweight website and database to simulate a simple access control or record-keeping platform.

## 🧠 Project Overview

The primary goal of this project is to create a secure, efficient facial recognition system with a graphical front-end for user interaction. This can be used for various applications such as check-in systems, secure logins, or personnel tracking.

The system uses Python and OpenCV to capture, train, and recognize faces. It stores and retrieves user records from a database and presents a user interface through a demo website hosted locally.

---

## 💡 Features

- ✅ Real-time facial recognition using OpenCV
- ✅ Image dataset generation from webcam
- ✅ Model training and face classification
- ✅ SQLite database to store user metadata
- ✅ Web interface (HTML/CSS/JavaScript) for demo purposes
- ✅ Included presentation and documentation

---

## 🗂 Repository Structure
SeniorCapstoneWebsite/
│
├── CaptureImages.py # Captures face images for training
├── TrainModel.py # Trains the recognizer with captured images
├── FaceRecognition.py # Performs real-time face recognition
│
├── Records.sql # SQL file to initialize or view user database
│
├── SeniorCapstoneDocumentation.docx # Final write-up of the project
├── Presentation.pdf # Capstone presentation slides
│
├── WebsiteDemo/ # Demo files for the local website
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md # Project overview (this file)



---

## 🚀 Getting Started

### 🛠 Prerequisites



Make sure the following are installed:

- Python 3.x
- OpenCV: `pip install opencv-python`
- SQLite or DB Browser for SQLite
- Webcam (internal or external)
- ultralytics
---

### 🧪 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RPGNorman/SeniorCapstoneWebsite.git
   cd SeniorCapstoneWebsite
   
python FaceRecognition.py


In googledrive 
AIMain.py show the rw AI usage without graphics(barebone)
## https://drive.google.com/drive/folders/1vozGF8MRHb9YXMWG15mFhOhxnr7FwBCN
.
├── app.py                    # Main application script
├── templates/
│   └── homepage.html         # Web interface
├── uploads/                  # Temporary image uploads
├── database/                 # Known face images
├── recognized_faces/         # Successfully recognized face crops
├── unrecognized_faces/       # Unrecognized face crops
├── static/
│   └── attendance/           # Annotated attendance images
├── students.xlsx             # Excel sheet with student names
├── attendancesheet.xlsx      # Automatically generated master attendance file

pip install these requirements

Flask
opencv-python
deepface
ultralytics
pandas
openpyxl
xlsxwriter


Install Python 3.9+

Clone this repo

Prepare the student database:

Place one clear image per student in the database/ folder.

The image filename (without extension) should match the name in students.xlsx.

Create students.xlsx

Include a column labeled "Student Name"

Example:

Student Name
Alice Johnson
Bob Smith

Run the App

bash
Copy
Edit
python app.py
Access the Web App

Go to http://localhost:5000

📷 How to Use
Go to the homepage

Upload a group photo with students

Recognized students will be marked and saved

A generated image with bounding boxes will appear

Attendance is automatically updated

📁 Output Files
attendancesheet.xlsx: Daily updated sheet tracking attendance by student and date

attendance_export_YYYYMMDD_HHMMSS.xlsx: Optional export files

attendance_YYYYMMDD_HHMMSS.jpg: Annotated photo of detections

✍️ TODO
Finish manual attendance submission (/submit_manual_attendance)

Improve UI

Add user authentication (optional)

Display attendance history on web interface

🔐 License
This project is provided for educational purposes. Contact the author for commercial use.
