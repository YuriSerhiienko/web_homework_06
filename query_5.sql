-- query_5.sql

SELECT subjects.id AS subject_id, subjects.subject AS subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.teacher = 'Your Desired Teacher';