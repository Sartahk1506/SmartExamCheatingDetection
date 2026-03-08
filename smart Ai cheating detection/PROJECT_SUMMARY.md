# Smart Cheating Detection System - Project Summary

## What Has Been Completed

### 1. Core AI Modules ✓
- **Face Detection Module** (ai_modules/face_recognition_module.py)
  - Uses OpenCV Haar Cascades for face detection
  - LBPH Face Recognizer for identity verification
  
- **Eye Tracking Module** (ai_modules/eye_tracking_module.py)
  - MediaPipe Face Mesh for facial landmark detection
  - Detects head turns and suspicious gaze patterns
  
- **Audio Detection Module** (ai_modules/audio_detection_module.py)
  - PyAudio for real-time audio capture
  - RMS volume analysis to detect whispering/talking
  
- **Anomaly Detection Module** (ai_modules/anomaly_detection.py)
  - Isolation Forest ML algorithm
  - Behavioral pattern analysis

### 2. Database Layer ✓
- **Database Connection** (Database/db_connection.py)
  - MySQL connection manager
  
- **Data Models** (Database/models.py)
  - StudentModel: Register and retrieve students
  - ExamModel: Create and manage exams
  - EventModel: Log and retrieve cheating events
  
- **Database Schema** (schema.sql)
  - Students table with face encodings
  - Exams table
  - Exam_Attendance table
  - Cheating_Events table

### 3. Monitoring System ✓
- **Exam Monitor** (monitoring/exam_moniter.py)
  - Multi-threaded real-time monitoring
  - Integrates all AI modules
  - Automatic event logging
  - Live video display with status

### 4. REST API ✓
- **Flask Application** (app.py)
  - POST /register_student - Register with photo
  - POST /create_exam - Create exam session
  - POST /start_exam - Start monitoring
  - POST /stop_exam - Stop monitoring
  - GET /get_events/<exam_id> - Retrieve events

### 5. Utilities & Documentation ✓
- Helper functions (utils/helper.py)
- Comprehensive README.md
- Quick Start Guide (QUICKSTART.md)
- Installation Guide (INSTALL.md)
- Demo script (demo.py)
- API test script (test_api.py)
- Setup batch file (setup.bat)

## How to Use

### Quick Test (Recommended First):
```bash
# Open Anaconda Prompt
cd "c:\Users\Sarthak Shrivastva\OneDrive\Desktop\smart cheating detection"
python demo.py
```

### Full System:
1. Setup MySQL database
2. Update database credentials
3. Run: `python app.py`
4. Use API endpoints to manage exams

## Key Features

1. **Real-time Monitoring**: Live video processing with instant alerts
2. **Multi-modal Detection**: Face, eye, audio, and behavioral analysis
3. **Machine Learning**: Adaptive anomaly detection
4. **Database Logging**: All events stored for review
5. **REST API**: Easy integration with other systems
6. **Scalable**: Can monitor multiple students simultaneously

## Technology Stack

- **Backend**: Python, Flask
- **Database**: MySQL
- **Computer Vision**: OpenCV, MediaPipe
- **Machine Learning**: scikit-learn (Isolation Forest)
- **Audio**: PyAudio, SpeechRecognition

## Next Steps

1. Install dependencies using Anaconda Prompt
2. Run demo.py to test the system
3. Setup MySQL for full functionality
4. Customize detection thresholds as needed
5. Add frontend UI (optional)

## Notes

- PyAudio is optional - system works without audio detection
- Face recognition uses OpenCV (no CMake required)
- All modules are modular and can be used independently
- Designed for Windows but can be adapted for Linux/Mac

## Project Structure
```
smart cheating detection/
├── ai_modules/              # AI detection modules
│   ├── face_recognition_module.py
│   ├── eye_tracking_module.py
│   ├── audio_detection_module.py
│   └── anomaly_detection.py
├── Database/                # Database layer
│   ├── db_connection.py
│   └── models.py
├── monitoring/              # Monitoring logic
│   └── exam_moniter.py
├── utils/                   # Utilities
│   └── helper.py
├── app.py                   # Flask REST API
├── demo.py                  # Standalone demo
├── test_api.py             # API testing
├── schema.sql              # Database schema
├── requirements.txt        # Dependencies
├── setup.bat               # Setup script
├── README.md               # Main documentation
├── QUICKSTART.md          # Quick start guide
└── INSTALL.md             # Installation guide
```

## Support

For issues:
1. Check INSTALL.md for common problems
2. Verify all dependencies are installed
3. Ensure camera/microphone permissions
4. Check MySQL connection if using database
