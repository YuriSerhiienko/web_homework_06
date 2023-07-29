-- query_1.sql

SELECT students.id, students.student, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.student
ORDER BY avg_grade DESC
LIMIT 5;