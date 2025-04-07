-- Host: local instance 3306
-- Password: NPstar123

-- Create the database
CREATE DATABASE IF NOT EXISTS RECORDS;
USE RECORDS;

-- Create Students table
CREATE TABLE Students (
    r_number INT PRIMARY KEY not null,
    first_name VARCHAR(50) not null,
    middle_name VARCHAR(50) not null,
    last_name VARCHAR(50) not null,
    email VARCHAR(100) UNIQUE not null
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY not null,
    course_name VARCHAR(100) not null,
    instructor_id INT UNIQUE not null,
    instructor_name VARCHAR(100) not null
);

-- Create Attendance table
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT not null,
    r_number INT not null,
    course_id INT not null,
    instructor_id INT not null,
    attendance_status BOOLEAN default FALSE,
    date DATE,
    time TIME,
    FOREIGN KEY (r_number) REFERENCES Students(r_number),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Courses(instructor_id)
);
-
-- INSERT into Student 
INSERT INTO Students (r_number, first_name, middle_name, last_name, email) VALUES
(11738979, 'Nivedita', 'NULL', 'Prabhu', 'nprabhu@ttu.edu'),
(11758567, 'Matthew', 'Land', 'Willingham', 'wil77411@ttu.edu'),
(11764742, 'Ayodeji', 'Joseph', 'Adeogun', 'aadeogun@ttu.edu'),
(11772596, 'Nicholas', 'Scott', 'Marshall', 'nichmars@ttu.edu'),
(11669553, 'Frank', 'NULL', 'Diabour', 'fdiabour@ttu.edu');

-- INSERT into Courses
INSERT INTO Courses (course_id, course_name, instructor_id, instructor_name) VALUES
(4366, 'Senior Capstone Project', 55663312, 'Victor Sheng');

-- INSERT into Attendance
INSERT INTO Attendance (r_number, course_id, instructor_id, attendance_status, date, time) VALUES
(11738979, 4366, 55663312, TRUE, STR_TO_DATE('2/4/2025', '%m/%d/%Y'), STR_TO_DATE('12:30:05', '%H:%i:%s')),
(11758567, 4366, 55663312, FALSE, NULL, NULL),
(11764742, 4366, 55663312, TRUE, STR_TO_DATE('2/6/2025', '%m/%d/%Y'), STR_TO_DATE('12:35:23', '%H:%i:%s')),
(11758567, 4366, 55663312, FALSE, NULL, NULL),
(11669553, 4366, 55663312, TRUE, STR_TO_DATE('2/4/2025', '%m/%d/%Y'), STR_TO_DATE('13:00:52', '%H:%i:%s'));

-- Show Data

-- Students
SELECT 'Students' AS Section;
SELECT 
    CONCAT('R', r_number) AS r_number, 
    first_name, 
    middle_name, 
    last_name, 
    email 
FROM Students;
Select '';

-- Courses
SELECT 'Courses' AS Section;
SELECT
    CONCAT('CS', course_id) AS course_id, 
    course_name, 
    instructor_id, 
    instructor_name 
FROM Courses;
Select '';

-- Attendance
SELECT 'Attendance Table' AS Section;
SELECT 
    attendance_id, 
    CONCAT('R', r_number) AS r_number, 
    CONCAT('CS', course_id) AS course_id, 
    instructor_id, 
    CASE 
        WHEN attendance_status = 1 THEN 'TRUE' 
        ELSE 'FALSE' 
    END AS attendance_status,
    date, 
    time 
FROM Attendance;


