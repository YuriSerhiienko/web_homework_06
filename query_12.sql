-- query_12.sql

SELECT students.student AS student_name, grades.grade AS grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_number = groups.id
WHERE groups.group_number = 'Your Desired Group' AND subjects.subject = 'Your Desired Subject'
ORDER BY grades.date_received DESC
LIMIT 20;
