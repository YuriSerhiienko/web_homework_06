from conection import create_connection
from sqlite3 import Error

def execute_query(connection, sql_file):
    try:
        cursor = connection.cursor()

        # Відкриваємо SQL-файл і виконуємо запит
        with open(sql_file, 'r') as file:
            sql_query = file.read()
            cursor.execute(sql_query)

        # Виводимо результати запиту
        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
    except Error as e:
        print(e)

if __name__ == '__main__':
    # Задаємо ім'я SQL-файлу, який містить запит
    sql_file = "query_12.sql"
    #Laura Baker - Student, Carrie Adams - Teacher, Geoscientist - Subject

    with create_connection() as conn:
        if conn is not None:
            execute_query(conn, sql_file)
        else:
            print("Connection is None")
