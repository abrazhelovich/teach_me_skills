import psycopg2
from psycopg2 import OperationalError


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database="jiradb",
            user="andrei",
            password="123456",
            host="127.0.0.1",
            port="5432"
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection
