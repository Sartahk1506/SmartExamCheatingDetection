# Getting Started - Smart Cheating Detection System

## 🚀 Quick Start (3 Steps)

### Step 1: Open Anaconda Prompt
- Press Windows Key
- Type "Anaconda Prompt"
- Open it (NOT regular Command Prompt)

### Step 2: Navigate to Project
```bash
cd "c:\Users\Sarthak Shrivastva\OneDrive\Desktop\smart cheating detection"
```

### Step 3: Run Demo
```bash
python demo.py
```

That's it! The demo will open your webcam and show real-time detection.

---

## 📋 What You Need

### Already Installed ✓
- Python (Anaconda)
- Most required packages (Flask, OpenCV, MediaPipe, etc.)

### Need to Install
Run this in Anaconda Prompt:
```bash
pip install Flask mysql-connector-python opencv-python opencv-contrib-python mediapipe scikit-learn SpeechRecognition Pillow Werkzeug
```

Or simply run:
```bash
launcher.bat
```
And select option 4 (Install Dependencies)

---

## 🎯 Usage Options

### Option 1: Demo Mode (Easiest)
No database needed. Just test the detection features.

**Run:**
```bash
python demo.py
```

**What it does:**
- Opens your webcam
- Detects faces in real-time
- Tracks eye movements
- Monitors audio (if available)
- Shows alerts on screen

**Controls:**
- Press 'q' to quit

---

### Option 2: Full System (Advanced)
Complete system with database, API, and multi-student support.

**Prerequisites:**
1. Install MySQL Server
2. Create database:
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Edit `Database/db_connection.py`:
   ```python
   password="your_mysql_password"
   ```

**Run:**
```bash
python app.py
```

**API will be available at:** http://localhost:5000

---

## 📡 API Usage

### 1. Register a Student
```bash
POST http://localhost:5000/register_student
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "course": "Computer Science",
  "photo_path": "path/to/student/photo.jpg"
}
```

### 2. Create an Exam
```bash
POST http://localhost:5000/create_exam
Content-Type: application/json

{
  "name": "Midterm Exam",
  "date": "2024-01-15",
  "duration": 120
}
```

### 3. Start Monitoring
```bash
POST http://localhost:5000/start_exam
Content-Type: application/json

{
  "student_id": 1,
  "exam_id": 1
}
```

### 4. Stop Monitoring
```bash
POST http://localhost:5000/stop_exam
Content-Type: application/json

{
  "student_id": 1,
  "exam_id": 1
}
```

### 5. Get Cheating Events
```bash
GET http://localhost:5000/get_events/1
```

---

## 🔧 Configuration

Edit `config.py` to customize:
- Database credentials
- Camera settings
- Detection thresholds
- Enable/disable features

---

## 🐛 Troubleshooting

### "No module named cv2"
**Solution:** Use Anaconda Prompt, not regular Command Prompt

### Camera not opening
**Solutions:**
1. Close other apps using camera (Zoom, Teams, etc.)
2. Check Windows camera permissions
3. Try different camera index in config.py (0, 1, 2)

### Audio not working
**Solution:** PyAudio is optional. System works without it.

### Database connection error
**Solutions:**
1. Verify MySQL is running
2. Check credentials in `Database/db_connection.py`
3. Ensure database 'exam_system' exists

---

## 📁 Project Files

- **demo.py** - Quick demo without database
- **app.py** - Full Flask application
- **launcher.bat** - Easy launcher menu
- **config.py** - Configuration settings
- **test_api.py** - API testing script
- **schema.sql** - Database schema

---

## 🎓 How It Works

1. **Face Detection**: Verifies student identity using OpenCV
2. **Eye Tracking**: Detects suspicious gaze using MediaPipe
3. **Audio Detection**: Identifies talking/whispering
4. **ML Anomaly Detection**: Learns normal behavior and flags anomalies

All events are logged to database for review.

---

## 📞 Need Help?

1. Read INSTALL.md for detailed installation
2. Check PROJECT_SUMMARY.md for complete overview
3. Review QUICKSTART.md for quick reference

---

## ✅ Next Steps

1. ✓ Run demo.py to test
2. ✓ Install MySQL (if needed)
3. ✓ Setup database
4. ✓ Run app.py
5. ✓ Test API endpoints
6. ✓ Customize config.py
7. ✓ Deploy for production use

---

**Enjoy using the Smart Cheating Detection System!** 🎉
