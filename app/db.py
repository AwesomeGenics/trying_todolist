import sqlite3

conn = sqlite3.connect('tasks.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
csr = conn.cursor()

csr.execute('''CREATE TABLE IF NOT EXISTS task_list(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)''')

csr.execute('''
CREATE TABLE IF NOT EXISTS owner_task(
    id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    owner TEXT NOT NULL)
''')

csr.execute('''
CREATE TABLE IF NOT EXISTS owner_task_done(
    id INTEGER PRIMARY KEY,
    task_name TEXT NOT NULL,
    owner TEXT NOT NULL)
''')