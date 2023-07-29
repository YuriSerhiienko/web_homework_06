from conection import create_connection  # Replace 'conection' with the correct module name
from sqlite3 import DatabaseError
from faker import Faker
from random import randint

fake = Faker()

def create_table(connection, sql_query, params):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, params)
    except DatabaseError as err:
        print(err)

if __name__ == "__main__":
    # Number of records to be generated for each table
    num_students = randint(30, 50)
    num_groups = 3
    num_subjects = randint(5, 8)
    num_teachers = randint(3, 5)
    num_grades_per_student = randint(10, 20)

    # Create students
    sql_create_students_table = """
        INSERT INTO students(student, group_number) VALUES (?, ?)
    """
    with create_connection() as conn:
        if conn is not None:
            groups = [i for i in range(1, num_groups + 1)]
            [create_table(conn, sql_create_students_table, params=(fake.name(), randint(1, num_groups))) for _ in range(num_students)]

            # Create groups
            sql_create_groups_table = """
                INSERT INTO groups(group_number) VALUES (?)
            """
            [create_table(conn, sql_create_groups_table, params=(i,)) for i in range(1, num_groups + 1)]

            # Create teachers
            sql_create_teachers_table = """
                INSERT INTO teachers(teacher) VALUES (?)
            """
            [create_table(conn, sql_create_teachers_table, params=(fake.name(),)) for _ in range(num_teachers)]

            # Create subjects
            sql_create_subjects_table = """
                INSERT INTO subjects(subject, teacher_id) VALUES (?, ?)
            """
            teachers = [i for i in range(1, num_teachers + 1)]
            [create_table(conn, sql_create_subjects_table, params=(fake.job(), randint(1, num_teachers))) for _ in range(num_subjects)]

            # Create grades
            sql_create_grades_table = """
                INSERT INTO grades(student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)
            """
            students = [i for i in range(1, num_students + 1)]
            subjects = [i for i in range(1, num_subjects + 1)]
            [create_table(conn, sql_create_grades_table, params=(randint(1, num_students), randint(1, num_subjects), randint(1, 100), fake.date_between(start_date='-1y', end_date='today'))) for _ in range(num_students * num_grades_per_student)]

        else:
            print("connection is None")
