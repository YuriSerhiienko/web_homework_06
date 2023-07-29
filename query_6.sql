-- query_6.sql

SELECT students.id AS student_id, students.student AS student_name
FROM students
JOIN groups ON students.group_number = groups.id
WHERE groups.group_number = 'Your Desired Group';