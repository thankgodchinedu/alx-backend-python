#!/usr/bin/env python3
import sqlite3
import functools

# Cache storage
query_cache = {}


def with_db_connection(func):
    """Decorator to provide a database connection"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


def cache_query(func):
    """Decorator to cache query results"""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Returning cached result")
            return query_cache[query]
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # First call: executes SQL and caches result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call: returns cached result
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
