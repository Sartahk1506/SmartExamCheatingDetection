import requests
import json

BASE_URL = "http://localhost:5000"

# Test 1: Register Student
print("Testing student registration...")
response = requests.post(f"{BASE_URL}/register_student", json={
    "name": "John Doe",
    "email": "john@example.com",
    "course": "Computer Science",
    "photo_path": "path/to/student/photo.jpg"
})
print(response.json())

# Test 2: Create Exam
print("\nTesting exam creation...")
response = requests.post(f"{BASE_URL}/create_exam", json={
    "name": "Midterm Exam",
    "date": "2024-01-15",
    "duration": 120
})
print(response.json())

# Test 3: Start Exam
print("\nTesting exam start...")
response = requests.post(f"{BASE_URL}/start_exam", json={
    "student_id": 1,
    "exam_id": 1
})
print(response.json())

# Test 4: Get Events
print("\nTesting get events...")
response = requests.get(f"{BASE_URL}/get_events/1")
print(response.json())
