#!/usr/bin/python3
"""
Module for task 2
"""
import sys
import MySQLdb


def main():
    """
    Main function to get state information from the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
            )
    cursor = connection.cursor()
    query = """
    SELECT *
    FROM states
    WHERE name = %s
    ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if cursor:
        cursor.close()
    if connection:
        connection.close()


if __name__ == "__main__":
    main()
