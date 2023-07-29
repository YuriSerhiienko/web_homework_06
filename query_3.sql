-- query_3.sql

SELECT groups.id AS group_id, groups.group_number AS group_name, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_number
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.subject = 'Your Desired Subject'
GROUP BY groups.id, groups.group_number;