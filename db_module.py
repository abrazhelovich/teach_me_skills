import sqlite3


def create_db(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products_table(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    number INT,
    comment TEXT);
    """)
    conn.commit()


def add_records(db_name, prods, table):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.executemany(f"INSERT INTO {table} VALUES(?, ?, ?, ?, ?);", prods)
    conn.commit()


def get_data(db_name, table):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table};")
    all_results = cur.fetchall()
    conn.commit()
    return all_results


def del_data(db_name, table, value):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table} WHERE id={value};")
    conn.commit()


def update_data(db_name, table, value, comment):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"UPDATE {table} SET {comment} WHERE id={value};")
    conn.commit()


