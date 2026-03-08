import cv2
import numpy as np

class FaceRecognitionModule:
    def __init__(self):
        self.known_encodings = []
        self.known_names = []
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.is_trained = False

    def load_student_face(self, photo_path, encoding):
        if encoding is not None:
            self.known_encodings.append(encoding)
            self.known_names.append("Student")
            if len(self.known_encodings) > 0:
                self.recognizer.train([encoding], np.array([0]))
                self.is_trained = True

    def detect_and_match(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return False, 0.0, None
        
        x, y, w, h = faces[0]
        face_roi = gray[y:y+h, x:x+w]
        
        if self.is_trained:
            label, confidence = self.recognizer.predict(face_roi)
            confidence_score = 1.0 - (confidence / 100.0)
            is_match = confidence < 70
            return is_match, confidence_score, (x, y, w, h)
        
        return True, 0.8, (x, y, w, h)