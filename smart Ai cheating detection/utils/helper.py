import cv2
import numpy as np

def save_frame(frame, filename):
    cv2.imwrite(filename, frame)

def resize_frame(frame, width=640):
    height = int(frame.shape[0] * (width / frame.shape[1]))
    return cv2.resize(frame, (width, height))
