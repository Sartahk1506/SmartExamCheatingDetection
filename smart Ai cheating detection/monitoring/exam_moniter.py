import cv2
import threading
import time
from ai_modules import FaceRecognitionModule, EyeTrackingModule, AudioDetectionModule, AnomalyDetector
from Database.models import EventModel

class ExamMonitor:
    def __init__(self, student_id, exam_id, camera_index=0):
        self.student_id = student_id
        self.exam_id = exam_id
        self.camera_index = camera_index
        self.running = False
        self.stop_event = threading.Event()
        
        self.face_module = FaceRecognitionModule()
        self.eye_module = EyeTrackingModule()
        self.audio_module = AudioDetectionModule()
        self.anomaly_detector = AnomalyDetector()
        self.feature_history = []

    def start(self, student_face_encoding):
        self.face_module.load_student_face(None, student_face_encoding)
        self.audio_module.start_listening()
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop)
        self.thread.start()

    def stop(self):
        self.running = False
        self.stop_event.set()
        self.audio_module.stop_listening()
        self.eye_module.close()
        if self.thread.is_alive():
            self.thread.join()

    def _monitor_loop(self):
        cap = cv2.VideoCapture(self.camera_index)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        while self.running and not self.stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                break

            is_known, confidence, location = self.face_module.detect_and_match(frame)
            if not is_known:
                EventModel.log_event(self.student_id, self.exam_id, "Face_Mismatch", confidence)
                print(f"⚠️ Unknown Face Detected!")

            is_eye_suspicious, gaze = self.eye_module.detect_eye_gaze(frame)
            if is_eye_suspicious:
                EventModel.log_event(self.student_id, self.exam_id, "Eye_Anomaly", 0.8)
                print(f"⚠️ Suspicious Eye Movement: {gaze}")

            is_audio_suspicious, volume = self.audio_module.detect_whisper()
            if is_audio_suspicious:
                EventModel.log_event(self.student_id, self.exam_id, "Whispering", volume/10000)
                print(f"⚠️ Audio Detected: {volume}")

            features = [0.5, 0.5, volume/10000] 
            self.anomaly_detector.add_sample(features)
            pred, score = self.anomaly_detector.predict(features)
            if pred == 1:
                EventModel.log_event(self.student_id, self.exam_id, "Behavioral_Anomaly", score)
                print(f"⚠️ ML Anomaly Detected: {score}")

            cv2.putText(frame, f"Student ID: {self.student_id}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Exam Monitor", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            time.sleep(0.1)

        cap.release()
        cv2.destroyAllWindows()