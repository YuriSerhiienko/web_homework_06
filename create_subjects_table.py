from conection import create_connection
from sqlite3 import DatabaseError

def create_table(conn, sql_query):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
    except DatabaseError as err:
            print(err)
            
if __name__ == "__main__":
    sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject VARCHAR(128),
            teacher_id INTEGER,
            FOREIGN KEY(teacher_id) REFERENCES teachers(id)
        );
    """
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_users_table)
        else:
             print("connection is None")