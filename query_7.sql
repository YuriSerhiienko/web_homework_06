-- query_7.sql

SELECT students.id AS student_id, students.student AS student_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_number = groups.id
WHERE groups.group_number = 'Your Desired Group' AND subjects.subject = 'Your Desired Subject';