import cv2
import numpy as np
from ai_modules import EyeTrackingModule, AudioDetectionModule, AnomalyDetector

print("Starting Demo Monitoring System...")
print("Press 'q' to quit")

# Initialize modules
eye_module = EyeTrackingModule()
audio_module = AudioDetectionModule()
anomaly_detector = AnomalyDetector()

# Start audio
try:
    audio_module.start_listening()
    audio_enabled = True
except:
    print("Audio not available, continuing without audio detection")
    audio_enabled = False

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Face Detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Eye Tracking
    is_suspicious, gaze = eye_module.detect_eye_gaze(frame)
    status_color = (0, 0, 255) if is_suspicious else (0, 255, 0)
    cv2.putText(frame, f"Gaze: {gaze}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
    
    # Audio Detection
    if audio_enabled:
        is_audio, volume = audio_module.detect_whisper()
        audio_status = "ALERT!" if is_audio else "Normal"
        cv2.putText(frame, f"Audio: {audio_status}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    cv2.putText(frame, "Demo Mode - Press 'q' to quit", (10, frame.shape[0]-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow("Smart Cheating Detection - Demo", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if audio_enabled:
    audio_module.stop_listening()
eye_module.close()

print("Demo ended")
