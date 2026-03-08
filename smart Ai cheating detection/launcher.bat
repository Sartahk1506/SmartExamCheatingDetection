@echo off
echo ========================================
echo Smart Cheating Detection System
echo ========================================
echo.
echo Select an option:
echo 1. Run Demo (No database required)
echo 2. Run Full System (Requires MySQL)
echo 3. Run API Tests
echo 4. Install Dependencies
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Starting Demo Mode...
    python demo.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Full System...
    python app.py
) else if "%choice%"=="3" (
    echo.
    echo Running API Tests...
    python test_api.py
) else if "%choice%"=="4" (
    echo.
    echo Installing Dependencies...
    pip install Flask mysql-connector-python opencv-python opencv-contrib-python mediapipe scikit-learn SpeechRecognition Pillow Werkzeug
    echo.
    echo Installation complete!
    pause
) else if "%choice%"=="5" (
    exit
) else (
    echo Invalid choice!
    pause
)
