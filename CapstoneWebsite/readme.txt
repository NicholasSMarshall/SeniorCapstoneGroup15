Capstone Attendance Tracking System – PythonAnywhere Deployment
This README provides a guide to accessing and testing our Flask-based attendance tracking system hosted on PythonAnywhere.

🔐 Login Credentials
To access the project:

Username: rpgmoose

Password: 7570OSGroup$

Log in at www.pythonanywhere.com/user/rpgmoose/

🔍 Navigating the PythonAnywhere Dashboard
Once logged in, the top navigation bar includes the following sections:

1. Dashboard
Default landing page — no interaction required.

2. Consoles
Can be ignored for this project.

3. Files
All project files are stored here:

Capstone/ – Main project directory:

app.py – The backend of the web application (Flask-based). Interfaces with both the MySQL database and AI models.

database/ – Stores face images recognized by YOLO and assigned an ID for DeepFace training.

models/ – Contains the YOLO model we trained.

recognized_faces/ – Contains YOLO-detected faces not yet assigned an ID.

static/attendance/ – Stores images captured for attendance tracking. Useful for audits or corrections.

templates/ – HTML frontend (with Jinja and JavaScript), calling API routes defined in app.py.

uploads/ – Temporarily stores uploaded images before processing.

4. deepface-env
Custom virtual environment with all necessary libraries installed:

DeepFace

YOLO

Flask, and others

🌐 Running the Web App
Click "Web" in the navigation bar.

Find your web app and click the Reload button.

⏳ Due to free-tier limitations, reloading takes ~30 seconds.

Once reloaded, follow the provided link to the live website and begin testing functionality.

🗄️ Accessing the Database
Navigate to "Databases".

Under Your Databases, click on:

rpgmoose$RECORDS

This opens a MySQL Console to interact with the backend database directly.

For easier navigation and understanding of relationships, refer to the provided ER Diagram.

👤 User Instructions
Once the site is live:

Launch the Website – Navigate to the live link after reloading.

Left Sidebar – Shows a list of students. Clicking a name will display that student’s attendance history.

Center Panel (Home) –

Upload one or more images with student faces.

Images will be processed, and attendance will be auto-marked.

Right Sidebar – Displays student names:

Red names = Not present.

Green names = Detected as present by YOLO + DeepFace.

You can manually change colors (toggle presence status).

Submit Attendance –

Once everyone is marked, click Submit.

The system records the current state (green = present, red = absent).

Only the latest submission counts — submitting again overrides the previous record.

Review Attendance – Click any student’s name on the left to view their individual attendance log.

❓ Need Help?
For any questions, issues, or clarifications, please feel free to reach out to our team. We're happy to assist!
