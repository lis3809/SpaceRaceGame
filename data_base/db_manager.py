import sqlite3


class DataBase:
    def __init__(self, file='data_base/players.db'):  # TODO
        self.__connection = sqlite3.connect(file)
        self.__cursor = self.__connection.cursor()

    def create_table(self, table_name):
        query_create = '''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            score_points INTEGER DEFAULT 0
        )
        '''.format(table_name)
        self.__cursor.execute(query_create)
        self.__connection.commit()

    def get(self, query='SELECT * FROM scores'):
        return self.__cursor.execute(query).fetchall()

    def insert(self, table_name, name, score):
        query_insert = f'''INSERT INTO {table_name} (name, score_points) VALUES 
            ('{name}', '{score}')
            '''
        self.__cursor.execute(query_insert)
        self.__connection.commit()

    def update_player_data(self, table_name, name, score):
        query_update = f'''UPDATE {table_name} SET score_points={score} WHERE name=\'{name}\' '''
        self.__cursor.execute(query_update)
        # Сохраняем изменения
        self.__connection.commit()

    def get_top_5_users(self, table_name):
        query_top_5 = f'''SELECT name, score_points FROM {table_name} ORDER BY score_points DESC LIMIT 5'''
        self.__cursor.execute(query_top_5)
        top_5_users = self.__cursor.fetchall()
        return top_5_users

    def get_best_player_score(self, table_name):
        query_best_player_score = f'''SELECT MAX (score_points) FROM {table_name} '''
        self.__cursor.execute(query_best_player_score)
        best_player_score = self.__cursor.fetchone()
        return best_player_score[0]

    def save_new_player(self, table_name, name):
        try:
            query_player = f'''INSERT INTO {table_name} (name) VALUES ('{name}')'''
            print(query_player)
            self.__cursor.execute(query_player)
            self.__connection.commit()
            return True
        except sqlite3.IntegrityError:
            print("Такой пользователь уже зарегистрирован")
            return False

    def get_user_score(self, table_name, name):
        query_user_score = f'''SELECT score_points FROM {table_name} WHERE name='{name}' '''
        self.__cursor.execute(query_user_score)
        user_score = self.__cursor.fetchone()
        return user_score[0]

    def __del__(self):
        print("Объект DataBase был уничтожен")
        self.__connection.close()
