from pathlib import Path

import sqlite3 as sql


class DbEngine:
    def __init__(self):
        self.db_path = "./src/data/main.db"

    def create_db(self, path: Path):
        with sql.connect(self.db_path) as mdb:
            cur = mdb.cursor()

            cur.execute('''CREATE TABLE IF NOT EXISTS history(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        num1 REAL NOT NULL,
                        operation TEXT NOT NULL,
                        num2 REAL NOT NULL,
                        result REAL NOT NULL,
                        timestamp TEXT NOT NULL
                        )''')
            
    def save_history(self, history):
        with sql.connect(self.db_path) as mdb:
            cur = mdb.cursor()

            try:
                cur.executemany(
                    'INSERT INTO history(num1, operation, num2, result, timestamp) VALUES (?,?,?,?,?)',
                    history
                )
            except Exception as e:
                raise e
    
    def get_history(self):
        with sql.connect(self.db_path) as mdb:
            cur = mdb.cursor()

            try:
                results = cur.execute('SELECT num1, operation, num2, result, timestamp FROM history').fetchall()

                print(results)
            except Exception as e:
                raise e
