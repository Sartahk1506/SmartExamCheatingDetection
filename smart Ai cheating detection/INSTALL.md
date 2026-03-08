# Installation Instructions

## Important: Python Environment

You have multiple Python installations. Use Anaconda Python for this project.

## Step 1: Verify Python Installation

Open Anaconda Prompt (not regular Command Prompt) and run:
```bash
python --version
where python
```

## Step 2: Install Dependencies

In Anaconda Prompt, navigate to project folder:
```bash
cd "c:\Users\Sarthak Shrivastva\OneDrive\Desktop\smart cheating detection"
```

Install all dependencies:
```bash
pip install Flask mysql-connector-python opencv-python opencv-contrib-python mediapipe scikit-learn SpeechRecognition Pillow Werkzeug
```

## Step 3: Test Installation

Run the demo:
```bash
python demo.py
```

## Step 4: Setup Database (Optional)

If you want to use the full system with database:

1. Install MySQL Server
2. Create database:
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Update password in `Database/db_connection.py`
4. Run Flask app:
   ```bash
   python app.py
   ```

## Common Issues

### Issue: "No module named cv2"
Solution: Make sure you're using Anaconda Prompt, not regular Command Prompt

### Issue: "No module named pip"
Solution: You're using the wrong Python. Use Anaconda Python (E:\anconda python\python.exe)

### Issue: PyAudio installation fails
Solution: PyAudio is optional. The system will work without it. Audio detection will be disabled.

### Issue: Camera not opening
Solution: 
- Close other applications using the camera
- Check camera permissions in Windows Settings
- Try different camera index (0, 1, 2) in the code

## Running the Project

### Quick Demo (No Database):
```bash
python demo.py
```

### Full System:
```bash
python app.py
```

Then use the API endpoints or run:
```bash
python test_api.py
```
