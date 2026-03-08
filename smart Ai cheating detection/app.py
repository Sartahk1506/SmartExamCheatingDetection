from flask import Flask, request, jsonify, send_from_directory
from Database.models import StudentModel, ExamModel, EventModel
from monitoring.exam_moniter import ExamMonitor
import mediapipe
import base64
import os
import numpy as np
import threading
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global dictionary to store active monitoring threads
active_exams = {}

def generate_face_encoding(image_path):
    """Generates face encoding from an image path"""
    try:
        image = mediapipe.load_image_file(image_path)
        encodings = mediapipe.face_encodings(image)
        if encodings:
            return encodings[0]
        return None
    except Exception as e:
        print(f"Error generating encoding: {e}")
        return None

@app.route('/register_student', methods=['POST'])
def register_student():
    """
    Register a new student with photo.
    Expects: Form data with 'name', 'email', 'course', and 'photo' (file)
    """
    if 'photo' not in request.files:
        return jsonify({"error": "No photo provided"}), 400
    
    file = request.files['photo']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save file
    filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Generate Face Encoding
    encoding = generate_face_encoding(filepath)
    if encoding is None:
        os.remove(filepath)
        return jsonify({"error": "No face detected in photo"}), 400

    # Convert encoding to bytes for MySQL BLOB

    # Save to DB
    student_id = StudentModel.register_student(
        name=request.form.get('name'),
        email=request.form.get('email'),
        course=request.form.get('course'),
        photo_path=filepath,
        face_encoding=None
    )

    if student_id:
        return jsonify({"message": "Student registered", "student_id": student_id}), 201
    else:
        return jsonify({"error": "Failed to register student"}), 500

@app.route('/create_exam', methods=['POST'])
def create_exam():
    """Create a new exam"""
    data = request.json
    exam_id = ExamModel.create_exam(
        name=data.get('exam_name'),
        date=data.get('exam_date'),
        duration=data.get('exam_duration')
    )
    if exam_id:
        return jsonify({"message": "Exam created", "exam_id": exam_id}), 201
    return jsonify({"error": "Failed to create exam"}), 500

@app.route('/assign_exam', methods=['POST'])
def assign_exam():
    """Assign an exam to a student"""
    data = request.json
    ExamModel.assign_exam(
        exam_id=data.get('exam_id'),
        student_id=data.get('student_id')
    )
    return jsonify({"message": "Exam assigned"}), 200

@app.route('/start_exam_monitoring', methods=['POST'])
def start_exam_monitoring():
    """
    Start the AI monitoring engine for a specific student.
    Expects: student_id, exam_id
    """
    data = request.json
    student_id = data.get('student_id')
    exam_id = data.get('exam_id')

    # Get student details including face encoding
    student = StudentModel.get_student_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    # Convert BLOB back to numpy array
    face_encoding = None
    if student.get('face_encoding'):
        face_encoding = np.frombuffer(student['face_encoding'], dtype=np.float32)

    # Start Monitor Thread
    monitor = ExamMonitor(student_id=student_id, exam_id=exam_id, camera_index=0)
    
    # Start in a daemon thread
    thread = threading.Thread(target=monitor.start, args=(face_encoding,))
    thread.daemon = True
    thread.start()

    active_exams[student_id] = monitor

    return jsonify({"message": "Monitoring started", "student_id": student_id}), 200

@app.route('/stop_exam_monitoring', methods=['POST'])
def stop_exam_monitoring():
    """Stop monitoring for a student"""
    data = request.json
    student_id = data.get('student_id')
    
    if student_id in active_exams:
        active_exams[student_id].stop()
        del active_exams[student_id]
        return jsonify({"message": "Monitoring stopped"}), 200
    return jsonify({"error": "No active monitoring found"}), 404

@app.route('/cheating_events', methods=['GET'])
def get_cheating_events():
    """Get all cheating events or filter by exam_id"""
    exam_id = request.args.get('exam_id')
    events = EventModel.get_events(exam_id=exam_id)
    return jsonify(events), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "System Online"}), 200

if __name__ == '__main__':
    print("Starting Smart Exam Detection System...")
    app.run(debug=True, port=5000)