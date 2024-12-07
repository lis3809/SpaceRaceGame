import sqlite3


class DataBase:
    def __init__(self, file='data_base/players.db'):  # TODO
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name):
        query_create = '''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_points INTEGER
        )
        '''.format(table_name)
        self.cursor.execute(query_create)
        self.connection.commit()

    def get(self, query='SELECT * FROM scores'):
        return self.cursor.execute(query).fetchall()

    def insert(self, table_name, name, score):
        query_insert = f'''INSERT INTO {table_name} (name, score_points) VALUES 
            ('{name}', '{score}')
            '''
        self.cursor.execute(query_insert)
        self.connection.commit()

    def __del__(self):
        print("Объект DataBase был уничтожен")
        self.connection.close()
