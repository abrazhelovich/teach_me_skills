from jira_board.cron.get_projects.db_connection import create_connection
from psycopg2 import Error


def add_rows(key, name):
    connection = create_connection()
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('SELECT * from JIRA_BOARD_JIRAUSER where account_id = %s', [key])

    data = cursor.fetchone()
    if data is None:
        try:
            cursor.execute('INSERT INTO JIRA_BOARD_JIRAUSER VALUES (%s, %s)', [name, key])
        except Error as e:
            print(e)


if __name__ == "__main__":
    add_rows()