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
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_number INTEGER
        );
    """
    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_users_table)
        else:
             print("connection is None")