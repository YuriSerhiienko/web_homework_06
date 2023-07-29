-- query_2.sql

SELECT students.id, students.student, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject = 'Your Desired Subject'
GROUP BY students.id, students.student
ORDER BY avg_grade DESC
LIMIT 1;