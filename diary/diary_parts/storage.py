if __name__ =='__main__':
    print('Модуль связи с SQLite для diary.py')

import sqlite3
from datetime import date, time
sql_select='''SELECT id, status, task, taskdate FROM diary'''

def dict_factory(cursor, row):
    d={}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d

def initialize(conn):
    with conn:
        conn.executescript('''CREATE TABLE IF NOT EXISTS diary(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 status TEXT NOT NULL,
 task TEXT NOT NULL,
 taskdate TEXT NOT NULL
 )''')


def connect(db_name=None):
    if db_name is None:
        db_name = 'diaryq'

    conn=sqlite3.connect(db_name)
    conn.row_factory=dict_factory

    return conn



def add_entry(conn, task, tdate, status):
    cursor = conn.execute("INSERT INTO diary (status, task, taskdate) VALUES (?,?,?)",(status, task, tdate))
    conn.commit()

def find_all_by_date(conn, tdate):
    with conn:    
        cursor = conn.execute(sql_select + ''' WHERE taskdate=?''',(tdate,))
        fo=cursor.fetchall()
        return fo

def find_by_pk(conn, pk):
    with conn:
        cursor = conn.execute(sql_select + ' WHERE id = ?', (pk,))
        return cursor.fetchone()

def change_status(conn, status, pk):
    with conn:
        cursor = conn.execute('''UPDATE diary SET status=? WHERE id=?''', (status, pk))
        conn.commit()
        return pk

def change_task (conn, data, pk):
    with conn:
        cursor = conn.execute('''UPDATE diary SET task=? WHERE id=?''', (data,pk))
        conn.commit()
        return pk
__all__=['initialize', 'connect', 'add_entry', 'find_all_by_date', 'find_by_pk', 'change_status', 'change_task']
