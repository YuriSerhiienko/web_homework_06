-- query_11.sql

SELECT teachers.teacher AS teacher_name, students.student AS student_name, AVG(grades.grade) AS avg_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE teachers.teacher = 'Your Desired Teacher' AND students.student = "Your Desired Student"
GROUP BY teachers.teacher, students.student;