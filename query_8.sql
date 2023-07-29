-- query_8.sql

SELECT teachers.id AS teacher_id, teachers.teacher AS teacher_name, AVG(grades.grade) AS avg_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.teacher = "Your Desired Teacher"
GROUP BY teachers.id, teachers.teacher;