import mediapipe as mp
import cv2
import numpy as np

class EyeTrackingModule:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_eye_gaze(self, frame):
        """
        Detects if eyes are looking away from the center.
        Returns: (is_suspicious, gaze_direction)
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if not results.multi_face_landmarks:
            return False, "No Face"

        landmarks = results.multi_face_landmarks[0].landmark

        # Approximate eye center (Landmark 468 is nose tip, 33/133 are eyes)
        # Simplified logic: Check if eye landmarks are significantly shifted
        # In a real app, calculate Pupil Center vs Eye Corners
        
        # For this demo, we check if the head is turned too much (Nose tip X position)
        nose_x = landmarks[4].x
        center_x = 0.5
        
        # If nose is too far left or right, head is turned
        if abs(nose_x - center_x) > 0.2:
            return True, "Head Turned"
            
        return False, "Normal"

    def close(self):
        self.face_mesh.close()