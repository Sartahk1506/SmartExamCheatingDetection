from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        # Initialize model
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.is_trained = False
        self.baseline_data = []

    def add_sample(self, features):
        """
        Add a feature vector (e.g., [head_angle, eye_gaze, audio_level])
        """
        self.baseline_data.append(features)
        if len(self.baseline_data) > 50: # Train after collecting some data
            self.train()

    def train(self):
        if len(self.baseline_data) < 10:
            return
        X = np.array(self.baseline_data)
        self.model.fit(X)
        self.is_trained = True

    def predict(self, features):
        """
        Returns 1 if anomaly, -1 if normal.
        """
        if not self.is_trained:
            return 0 # Unknown
        X = np.array([features])
        prediction = self.model.predict(X)
        score = self.model.score_samples(X)[0]
        return prediction, score