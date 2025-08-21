import face_recognition
import cv2
import os
import sys
import tkinter as tk
from tkinter import messagebox
from deepface import DeepFace

THRESHOLD = 0.35

img1 = "Sean.jpg"

enc1 = face_recognition.face_encodings(img1)[0]

def capture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
    return

    ok, frame = cap.read()

    cap.release()
    if not ok:
        raise RuntimeError("Failed to read frame from webcam")
    return frame

def verifye_user():
    if not os.path.exists(img1):
        raise FileNotFoundError("Could not fine the image")
    frame = capture()
    temp_path = "_life.jpg"
    cv2.imwrite(temp_path, frame)
    result = DeepFace.verify(img1_path = img1, img2_path = temp_path, detector_backend = "retinaface", distance_metric = "cosine", enforce_detection = False)
    os.remove(temp_path)
    return result["verified"] and result["distance"] <= THRESHOLD

def app():
    window = tk.Tk()
    window.geometry("800x800")
    window.title("Face Unlocker App")


    window.mainloop()

if __name__ == "__main__":
    ret = verifye_user()
    if ret:
        app()
    else:
        print("No match")





