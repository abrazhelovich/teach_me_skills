from conn_postgres import create_connection


def add_rows(number, key, name):
    connection = create_connection()
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('SELECT * from JIRA_BOARD_PROJECT where prject_id = %s', [number])

    data = cursor.fetchone()
    if data is None:
        print('There is no component named %s' % number)
        cursor.execute('INSERT INTO JIRA_BOARD_PROJECT (prject_id, key, name) VALUES (%s, %s, %s)', [number, key, name])


if __name__ == "__main__":
    add_rows()