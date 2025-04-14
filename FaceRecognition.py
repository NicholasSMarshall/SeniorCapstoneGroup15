import os
import cv2
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from deepface import DeepFace
from ultralytics import YOLO
from datetime import datetime

# Load YOLOv8 face detection model
model = YOLO('yolov8n-face.pt')  # Ensure this model file exists

# Create output folders if they don't exist
output_folder = 'recognized_faces'
attendance_folder = 'ATTENDANCE'
os.makedirs(output_folder, exist_ok=True)
os.makedirs(attendance_folder, exist_ok=True)

# Load the image
image_path = 'NEWIMAGE.jpeg'  # Ensure this path is correct
image = cv2.imread(image_path)

# Detect faces using YOLOv8
results = model(image, conf=0.1)

# Process each detected face for recognition
for idx, result in enumerate(results[0].boxes):
    x1, y1, x2, y2 = map(int, result.xyxy[0].tolist())  # Extract coordinates

    # Crop the detected face region
    face_image = image[y1:y2, x1:x2]

    # Save the cropped face temporarily for DeepFace
    temp_face_path = os.path.join(output_folder, f"temp_face_{idx}.jpg")
    cv2.imwrite(temp_face_path, face_image)

    identity = "DOES NOT EXIST"

    try:
        # Use DeepFace to recognize the face from the database
        recognition_result = DeepFace.find(img_path=temp_face_path, db_path="database")

        if len(recognition_result[0]) > 0:
            # Extract the identity of the recognized face
            identity = os.path.basename(recognition_result[0]['identity'][0])

            # Save recognized face with identity name
            file_name = f"{identity.replace(' ', '_')}.jpg"
            file_path = os.path.join(output_folder, file_name)
            cv2.imwrite(file_path, face_image)

            print(f"Saved {file_name} to {output_folder}")

    except ValueError:
        print(f"No face detected in face {idx}")

    # Draw bounding box and identity text
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box
    cv2.putText(image, identity, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Generate a unique filename based on the current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_image_path = os.path.join(attendance_folder, f"attendance_{timestamp}.jpg")

# Save the final output image in the ATTENDANCE folder
cv2.imwrite(output_image_path, image)
print(f"Final output image saved to {output_image_path}")

# -----------------------
# Create Tkinter GUI
# -----------------------
root = tk.Tk()
root.title("Scrollable Face Detection")

# Convert the image for Tkinter
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image_rgb)
image_tk = ImageTk.PhotoImage(image_pil)

# Create a frame with a canvas and scrollbars
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
scrollable_frame = ttk.Frame(canvas)

# Configure scroll region
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Add image label to scrollable frame
label = ttk.Label(scrollable_frame, image=image_tk)
label.image = image_tk  # Keep reference
label.pack()

# Place scrollbars
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run Tkinter main loop
root.mainloop()