@echo off
echo ========================================
echo Smart Cheating Detection System Setup
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
pip install Flask mysql-connector-python opencv-python mediapipe scikit-learn Pillow Werkzeug SpeechRecognition
echo.

echo Step 2: Setting up MySQL database...
echo Please run the following command manually:
echo mysql -u root -p ^< schema.sql
echo.

echo Step 3: Update database credentials...
echo Edit Database\db_connection.py and update your MySQL password
echo.

echo Setup complete!
echo Run 'python app.py' to start the application
pause
