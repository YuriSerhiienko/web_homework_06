-- query_9.sql

SELECT subjects.id AS subject_id, subjects.subject AS subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.student = "Your Desired Student"
GROUP BY subjects.id, subjects.subject;