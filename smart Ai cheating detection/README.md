# Smart Cheating Detection System

AI-powered exam monitoring system using face detection, eye tracking, audio detection, and anomaly detection.

## Features
- Face Detection: Verifies student identity using OpenCV
- Eye Tracking: Detects suspicious gaze patterns with MediaPipe
- Audio Detection: Identifies whispering/talking
- ML Anomaly Detection: Behavioral pattern analysis with Isolation Forest

## Setup

### 1. Install Dependencies
```bash
pip install Flask mysql-connector-python opencv-python mediapipe scikit-learn Pillow Werkzeug SpeechRecognition
```

Or run the setup script:
```bash
setup.bat
```

### 2. Setup MySQL Database
```bash
mysql -u root -p < schema.sql
```

### 3. Configure Database
Edit `Database/db_connection.py` and update:
```python
password="your_mysql_password"
```

### 4. Run Application
```bash
python app.py
```

## API Endpoints

### Register Student
```
POST /register_student
{
  "name": "John Doe",
  "email": "john@example.com",
  "course": "Computer Science",
  "photo_path": "path/to/photo.jpg"
}
```

### Create Exam
```
POST /create_exam
{
  "name": "Midterm Exam",
  "date": "2024-01-15",
  "duration": 120
}
```

### Start Monitoring
```
POST /start_exam
{
  "student_id": 1,
  "exam_id": 1
}
```

### Stop Monitoring
```
POST /stop_exam
{
  "student_id": 1,
  "exam_id": 1
}
```

### Get Cheating Events
```
GET /get_events/<exam_id>
```

## Project Structure
```
├── ai_modules/          # AI detection modules
│   ├── face_recognition_module.py
│   ├── eye_tracking_module.py
│   ├── audio_detection_module.py
│   └── anomaly_detection.py
├── Database/            # Database models and connection
├── monitoring/          # Exam monitoring logic
├── utils/              # Helper functions
├── app.py              # Flask application
├── schema.sql          # Database schema
└── requirements.txt    # Python dependencies
```

## Requirements
- Python 3.8+
- MySQL 8.0+
- Webcam
- Microphone (optional for audio detection)

## Notes
- PyAudio may require additional setup on Windows
- Press 'q' in the monitoring window to stop manually
- All cheating events are logged to the database
