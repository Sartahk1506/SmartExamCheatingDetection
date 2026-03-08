-- Create database
CREATE DATABASE IF NOT EXISTS smart_exam_monitoring;

-- Select database
USE smart_exam_monitoring;

-- Students Table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(100),
    photo_path VARCHAR(255),
    face_encoding LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exams Table
CREATE TABLE IF NOT EXISTS Exams (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_name VARCHAR(100) NOT NULL,
    exam_date DATE NOT NULL,
    exam_duration INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exam Attendance Table
CREATE TABLE IF NOT EXISTS Exam_Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_id INT NOT NULL,
    student_id INT NOT NULL,
    status VARCHAR(50) DEFAULT 'assigned',

    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
    ON DELETE CASCADE,

    FOREIGN KEY (student_id) REFERENCES Students(student_id)
    ON DELETE CASCADE
);

-- Cheating Events Table
CREATE TABLE IF NOT EXISTS Cheating_Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    confidence_score FLOAT,

    FOREIGN KEY (student_id) REFERENCES Students(student_id)
    ON DELETE CASCADE,

    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
    ON DELETE CASCADE
);
SHOW TABLES;

