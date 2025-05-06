# 🎓 **Smart Attendance System – Facial Recognition Attendance**

This repository contains a complete facial recognition-based attendance tracking system with a web interface, Excel reporting, and student database management.

![System Demo](https://via.placeholder.com/1200x400/2c3e50/ffffff?text=Smart+Attendance+System+Demo)  
*(Replace with actual demo GIF/screenshot)*

## 🫠 **Overview**

The **Smart Attendance System** leverages facial recognition technology to automate student attendance tracking. It includes features for processing classroom photos, identifying students, and managing attendance data with Excel export functionality.

### **Key Features:**
- 📸 **Classroom Photo Processing**: Process class photos for attendance tracking.
- 🧠 **AI-Powered Face Detection & Identification**: Use YOLOv8 for face detection and DeepFace for student identification.
- 🗂️ **Daily Attendance Records**: Track attendance automatically and update records.
- ✏️ **Manual Correction Interface**: Easily correct attendance data when needed.
- 📊 **Excel Report Generation**: Export attendance data for analysis and reporting.

### **Potential Use Cases:**
- 🎓 **University/College Attendance Systems**
- 💼 **Corporate Training Sessions**
- 🎟️ **Event Check-in Systems**

---

## 💡 **Features**

### **Core Features:**
| Feature | Description |
| ------- | ----------- |
| ✅ **Automated Face Detection** | Detects and identifies faces from classroom photos. |
| ✅ **Student Identification** | Matches faces with student profiles for attendance. |
| ✅ **Present/Absent Tracking** | Automatically records attendance based on face matching. |
| ✅ **Manual Attendance Adjustment** | Allows manual edits of attendance records. |
| ✅ **Daily/Exportable Reports** | Generate attendance reports in Excel format. |

### **Technical Features:**
| Feature | Description |
| ------- | ----------- |
| 🖥️ **Flask Web Interface** | Simple web interface for managing attendance. |
| 📊 **Pandas Excel Integration** | Use Pandas to manage and export Excel files. |
| 🧠 **YOLOv8 Face Detection** | State-of-the-art face detection technology. |
| 🔍 **DeepFace Recognition** | AI-powered student face recognition. |
| 🖼️ **OpenCV Image Processing** | Process and annotate student images. |

---

## 🗂️ **Repository Structure**

```plaintext
smart-attendance-system/
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── yolov8n-face.pt          # Face detection model
├── students.xlsx            # Student roster (names match image filenames)
├── attendancesheet.xlsx     # Master attendance file (auto-generated)
│
├── database/                # Known face images (1+ images per student)
├── uploads/                 # Temporary upload storage
├── recognized_faces/        # Cropped recognized faces
├── unrecognized_faces/      # Cropped unrecognized faces
│
├── static/                  
│   ├── styles.css           # Custom styles
│   └── attendance/          # Processed attendance images
│
└── templates/
    └── homepage.html        # Web interface template
🚀 Getting Started
🛠 Prerequisites
Python 3.9+

Webcam (for real-time capture option)

Modern web browser

🔧 Installation
Clone the repository:


git clone https://github.com/yourusername/smart-attendance-system.git
cd smart-attendance-system
Create a virtual environment:


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Download the face detection model:


wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n-face.pt
Database Setup:

Add student face images to the database/ folder using the naming format: Firstname_Lastname.jpg.

Update students.xlsx to match student names with image filenames.

Run the application:


python app.py
📷 How to Use
Access the Web Interface:
Visit the web app at http://localhost:5000.

Upload a Class Photo:
Upload a photo of the class containing students' faces.

System Process:

The system will automatically detect faces in the image.

It will match the faces against the known student database.

The attendance records will be updated based on the identified students.

You can manually adjust any incorrect identifications.

Export Attendance Report:
Generate and export attendance records as Excel files when needed.

📁 Output Files
File Type	Location	Description
Master Attendance	attendancesheet.xlsx	Complete attendance history
Export Reports	attendance_export_*.xlsx	Dated attendance snapshots
Processed Images	static/attendance/attendance_*.jpg	Annotated images with detected faces

✍️ Future Work
Real-time camera feed processing.

Student attendance history dashboard.

Multi-class support.

Enhanced admin interface for easier management.

Mobile responsiveness improvements.

🔐 License
This project is licensed under the MIT License. See the LICENSE file for details. Educational use is encouraged; commercial use requires permission.
