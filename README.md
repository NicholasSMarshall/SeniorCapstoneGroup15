# 🎓 Senior Capstone Website – Facial Recognition Attendance System

This repository contains the full implementation and documentation for our Senior Capstone Project — a facial recognition-based attendance tracking system with a web-based interface and database integration.

---

## 🫠 Overview

The goal of this project is to create a secure, efficient facial recognition system with a graphical front-end. It can be adapted for:

* Student attendance systems
* Personnel check-ins
* Secure login platforms

The system uses Python, OpenCV, and DeepFace for recognition and integrates with a Flask web app and SQLite for data management.

---

## 💡 Features

✅ Real-time facial recognition (OpenCV + DeepFace)
✅ Image dataset generation and model training
✅ SQLite database for user metadata
✅ Web-based UI using Flask + HTML/CSS/JS
✅ Excel attendance record generation
✅ Auto-detection and classification of students
✅ Included presentation and final documentation

---

## 🗂️ Repository Structure

```
SeniorCapstoneWebsite/
├── CaptureImages.py              # Captures face images for training
├── TrainModel.py                 # Trains the recognizer with captured images
├── FaceRecognition.py           # CLI-based real-time face recognition
│
├── app.py                        # Web-based Flask app with attendance logic
├── students.xlsx                 # Student list (names should match image filenames)
├── attendancesheet.xlsx         # Master attendance file (auto-generated)
│
├── database/                     # Known face images (1 image per student)
├── uploads/                      # Temporary upload storage for test images
├── recognized_faces/            # Cropped, recognized faces
├── unrecognized_faces/          # Cropped, unrecognized faces
├── static/
│   └── attendance/              # Annotated attendance images
├── templates/
│   └── homepage.html            # Web interface
│
├── WebsiteDemo/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Records.sql                  # SQLite setup script
├── Presentation.pdf             # Final capstone presentation
├── SeniorCapstoneDocumentation.docx  # Project write-up
└── README.md                    # This file
```

---

## 🚀 Getting Started

### 🛠 Prerequisites

Make sure the following are installed:

* Python 3.9+
* A webcam (internal/external)
* SQLite or DB Browser for SQLite

Install required Python libraries:

```bash
pip install Flask opencv-python deepface ultralytics pandas openpyxl XlsxWriter
```

---

### 🔧 Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/RPGNorman/SeniorCapstoneWebsite.git
   cd SeniorCapstoneWebsite
   ```

2. **Prepare the student database**

   * Add one clear image per student to the `database/` folder.
   * The filename (e.g., `Alice_Johnson.jpg`) should match exactly with the student’s name in `students.xlsx`.

3. **Create `students.xlsx`**

   ```plaintext
   Student Name
   Alice Johnson
   Bob Smith
   ...
   ```

---

### 🧪 Running the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📷 How to Use

1. Go to the homepage.
2. Upload a group photo containing students.
3. Recognized students will be marked in the image.
4. Attendance is recorded in `attendancesheet.xlsx`.
5. Cropped recognized/unrecognized face images are saved for review.

---

## 📁 Output Files

* `attendancesheet.xlsx` — Rolling attendance tracking by date.
* `attendance_export_YYYYMMDD_HHMMSS.xlsx` — Exported attendance snapshots.
* `attendance_YYYYMMDD_HHMMSS.jpg` — Annotated detection images.

---

## 📂 Additional (Google Drive Link)

* Barebones version (`AIMain.py`) without the web interface is available here:
  🔗 [Google Drive Folder](https://drive.google.com/drive/folders/1vozGF8MRHb9YXMWG15mFhOhxnr7FwBCN)

---

## ✍️ TODO (Future Work)

* [ ] Manual attendance submission page (`/submit_manual_attendance`)
* [ ] Improve front-end UI and styling
* [ ] Add user authentication
* [ ] Display attendance history on the dashboard

---

## 🔐 License

This project is intended for educational use only. Please contact the authors for any commercial or derivative use.
