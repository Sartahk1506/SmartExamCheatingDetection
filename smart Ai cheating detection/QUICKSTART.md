# Quick Start Guide

## Option 1: Run Demo (No Database Required)

Test the monitoring system without setting up the database:

```bash
python demo.py
```

This will:
- Open your webcam
- Detect faces
- Track eye movements
- Monitor audio (if available)
- Display real-time alerts

Press 'q' to quit.

## Option 2: Full System Setup

### Step 1: Install MySQL
Download and install MySQL from https://dev.mysql.com/downloads/

### Step 2: Create Database
```bash
mysql -u root -p < schema.sql
```

### Step 3: Configure Database Connection
Edit `Database/db_connection.py`:
```python
password="your_mysql_password"
```

### Step 4: Run Flask Application
```bash
python app.py
```

The API will be available at http://localhost:5000

### Step 5: Test API
```bash
python test_api.py
```

## Troubleshooting

### Camera not working
- Check if another application is using the camera
- Try changing camera_index in ExamMonitor (0, 1, 2, etc.)

### Audio not working
- PyAudio may need additional setup on Windows
- The system will work without audio detection

### Database connection error
- Verify MySQL is running
- Check credentials in db_connection.py
- Ensure database 'exam_system' exists

## Project Components

1. **ai_modules/** - Detection algorithms
   - Face detection using OpenCV Haar Cascades
   - Eye tracking using MediaPipe Face Mesh
   - Audio detection using PyAudio
   - Anomaly detection using Isolation Forest

2. **Database/** - Data persistence
   - Student registration
   - Exam management
   - Event logging

3. **monitoring/** - Real-time monitoring
   - Multi-threaded exam monitoring
   - Real-time video processing
   - Event detection and logging

4. **app.py** - REST API
   - Student registration endpoint
   - Exam management endpoints
   - Monitoring control endpoints
