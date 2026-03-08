from .db_connection import DatabaseManager
import hashlib

db = DatabaseManager()

class StudentModel:
    @staticmethod
    def register_student(name, email, course, photo_path, face_encoding):
        conn = db.get_connection()
        cursor = conn.cursor()
        try:
            # Hash password (placeholder for login system)
            password_hash = hashlib.sha256(b"password123").hexdigest() 
            
            cursor.execute("""
                INSERT INTO Students (student_name, email, course, photo_path, face_encoding)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, email, course, photo_path, face_encoding))
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error registering student: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def get_student_by_id(student_id):
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Students WHERE student_id = %s", (student_id,))
        return cursor.fetchone()

class ExamModel:
    @staticmethod
    def create_exam(name, date, duration):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Exams (exam_name, exam_date, exam_duration)
            VALUES (%s, %s, %s)
        """, (name, date, duration))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def assign_exam(exam_id, student_id):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Exam_Attendance (exam_id, student_id)
            VALUES (%s, %s)
        """, (exam_id, student_id))
        conn.commit()

class EventModel:
    @staticmethod
    def log_event(student_id, exam_id, event_type, confidence_score):
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Cheating_Events (student_id, exam_id, event_type, timestamp, confidence_score)
            VALUES (%s, %s, %s, NOW(), %s)
        """, (student_id, exam_id, event_type, confidence_score))
        conn.commit()

    @staticmethod
    def get_events(exam_id=None):
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        if exam_id:
            cursor.execute("SELECT * FROM Cheating_Events WHERE exam_id = %s", (exam_id,))
        else:
            cursor.execute("SELECT * FROM Cheating_Events")
        return cursor.fetchall()