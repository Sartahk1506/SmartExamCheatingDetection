# Configuration File for Smart Cheating Detection System

# Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"  # CHANGE THIS
DB_NAME = "exam_system"

# Camera Configuration
CAMERA_INDEX = 0  # 0 for default camera, 1 for external camera, etc.
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Detection Thresholds
FACE_CONFIDENCE_THRESHOLD = 70  # Lower = stricter matching
EYE_GAZE_THRESHOLD = 0.2  # Head turn threshold
AUDIO_THRESHOLD = 3000  # Audio volume threshold for whispering detection

# Anomaly Detection
ANOMALY_CONTAMINATION = 0.1  # Expected proportion of anomalies (10%)
ANOMALY_TRAINING_SAMPLES = 50  # Samples needed before training

# Flask Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# Monitoring Configuration
MONITORING_FPS = 10  # Frames per second to process
ENABLE_AUDIO_DETECTION = True
ENABLE_EYE_TRACKING = True
ENABLE_FACE_DETECTION = True
ENABLE_ANOMALY_DETECTION = True

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "exam_monitoring.log"

# Event Types
EVENT_TYPES = {
    "FACE_MISMATCH": "Unknown face detected",
    "EYE_ANOMALY": "Suspicious eye movement",
    "WHISPERING": "Audio detected",
    "BEHAVIORAL_ANOMALY": "Unusual behavior pattern"
}
