import sqlite3
sql_select='''SELECT
                    id
                    status
                    task
                    tasktime
                    created
               FROM
                    diary
'''


def initialize(conn):
    with conn:
        conn.executescript('''CREATE TABLE IF NOT EXISTS diary(
                           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
                           status INTEGER NOT NULL DEFAULT 0
                           task TEXT NOT NULL
                           tasktime DATETIME NOT NULL
                           created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn=sqlite3.connect(db_name)
    conn.row_factory=dict_factory

    return conn

def dict_factory(cursor, row):
    d={}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
        return d

def add_entry(conn, task, ttime):
    cursor = conn.execute('''INSERT INTO diary (task, ttime) VALUES (?)
                          ''', (task, ttime))

def find_all_by_date(conn,date=None):
    if date is None:
        date=() #date=(сегодня) пока не разобрался с datetime и форматом ввода даты
    with conn:
        cursor = conn.execute(sql_select + ' WHERE tasktime = ?',(date,))
        return cursor.fetchall()

def find_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(sql_select + ' WHERE id = ?', (pk,))
        return cursor.fetchone()

def change_status(conn, status, pk):
    with conn:
        cursor = conn.execute('''UPDATE diary SET status=? WHERE pk=?''', (status, pk))
        return pk

def change_task (conn, task, pk):
    with conn:
        cursor = conn.execute('''UPDATE diary SET task=? WHERE pk=?''', (task,pk))
        return pk
