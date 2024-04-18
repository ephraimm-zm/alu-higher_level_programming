#!/usr/bin/python3
"""
List all states from the specified database.
"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """Connect to the database and list all states sorted by ID."""
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    """Main function."""
    username= sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(username, password, database_name)
