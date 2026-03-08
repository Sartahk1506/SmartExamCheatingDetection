import pyaudio
import numpy as np

class AudioDetectionModule:
    def __init__(self, threshold=3000):
        self.threshold = threshold
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.is_listening = False

    def start_listening(self):
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.is_listening = True

    def detect_whisper(self):
        """
        Detects if audio volume exceeds threshold (indicating speech/whispering).
        """
        if not self.is_listening:
            return False, 0.0
        
        data = self.stream.read(1024, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        rms = np.sqrt(np.mean(audio_data**2))
        
        is_suspicious = rms > self.threshold
        return is_suspicious, rms

    def stop_listening(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()