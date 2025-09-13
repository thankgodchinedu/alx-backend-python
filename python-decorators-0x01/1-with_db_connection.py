#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime   # for consistent logging

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Opening database connection...")
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
            print(f"[{datetime.now()}] Database connection closed.")
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)

