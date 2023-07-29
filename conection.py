import sqlite3
from contextlib import contextmanager

@contextmanager
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("university.db")
        yield connection
        connection.commit()
    except Exception as err:
        print(err)
        connection.rollback()
    finally:
        connection.close()