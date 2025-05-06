🎓 Senior Capstone Website – Facial Recognition Attendance System
This repository contains the full implementation and documentation for our Senior Capstone Project — a facial recognition-based attendance tracking system with a web-based interface and database integration.
---

## 🫠 Overview

The goal of this project is to create a secure, efficient facial recognition system with a graphical front-end. It can be adapted for:

* Student attendance systems
* Personnel check-ins
* Secure login platforms

Both systems use Python, OpenCV, and DeepFace for recognition. The Localhost integrates with a Flask web app and SQLite for data management, while the website uses Pythonanywhere pulling from the stored files. 

---

## 💡 Features

✅ Real-time facial recognition (OpenCV + DeepFace)
✅ Image dataset generation and model training
✅ SQLite database for user metadata
✅ Web-based UI using Flask + HTML/CSS/JS
✅ Excel attendance record generation
✅ Auto-detection and classification of students
✅ Included presentations and final documentations

---

## 🗂️ Repository Structure

```
SeniorCapstoneWebsite - CapstoneWebsite
├── Capstone                      # Main project directory:
├── app.py                        # The backend of the web application (Flask-based). Interfaces with both the MySQL database and AI models.
├── database                      # Stores face images recognized by YOLO and assigned an ID for DeepFace training.
├── models                        # Contains the YOLO model we trained.
├── recognized_faces              # Contains YOLO-detected faces not yet assigned an ID.
├── static/attendance             # Stores images captured for attendance tracking. Useful for audits or corrections.
├── templates                     # HTML frontend (with Jinja and JavaScript), calling API routes defined in app.py.
├── uploads                       # Temporarily stores uploaded images before processing.


SeniorCapstoneLocalhost - CapstoneApp
├── CaptureImages.py              # Captures face images for training
├── TrainModel.py                 # Trains the recognizer with captured images
├── FaceRecognition.py            # CLI-based real-time face recognition
│
├── app.py                        # Web-based Flask app with attendance logic
├── students.xlsx                 # Student list (names should match image filenames)
├── attendancesheet.xlsx          # Master attendance file (auto-generated)
│
├── database/                     # Known face images (1 image per student)
├── uploads/                      # Temporary upload storage for test images
├── recognized_faces/             # Cropped, recognized faces
├── unrecognized_faces/           # Cropped, unrecognized faces
├── static/
│   └── attendance/               # Annotated attendance images
├── templates/
│   └── homepage.html             # Web interface
│
├── WebsiteDemo/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Localhost Demo Files          # Link to the google drive of the files
├── README.md                     # This file
├── Records.sql                   # SQLite setup script
└── Website Link for Demo         # Normal Link to the website 
```

---

## 🚀 Getting Started

---
Depending on which one you want to test, their prerequisites and steps will be in their respective directories
### CapstoneWebsite
### CapstoneApp

### 🧪 Running the Capstone App

Follow the prerequisites and steps in the directory

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧪 Running the Capstone Website

Log in at www.pythonanywhere.com/user/rpgmoose/ with the password provided in the directory

Normal website: https://www.pythonanywhere.com/user/rpgmoose/

---

## 📷 How to Use

1. Go to the homepage.
2. Upload a group photo containing students.
3. Recognized students will be marked in the image.
4. Attendance is stored in their respective files.
5. Cropped recognized/unrecognized face images are saved for review.

---

---

## ✍️ TODO (Future Work)

* [ ] Manual attendance submission page (`/submit_manual_attendance`)
* [ ] Improve front-end UI and styling
* [ ] Add user authentication
* [ ] Display attendance history on the dashboard

---

## 🔐 License

This project is intended for educational use only. Please contact the authors for any commercial or derivative use.
