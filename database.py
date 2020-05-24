import mysql.connector #https://dev.mysql.com/doc/connector-python/en/
import json


class Database:
    def __init__(self, db_name=None):
        configs = self._get_configs()
        self._cnx = mysql.connector.connect(
            user=configs['mysql']['user'],
            password=configs['mysql']['passwd'],
            host=configs['mysql']['host'],
            database=db_name or ()
        )
        self._cursor = self._cnx.cursor()

    @property
    def connection(self):
        return self._cnx

    @property
    def cursor(self):
        return self._cnx.cursor()

    def _get_configs(self):
        with open("config.json") as data:
            configs = json.load(data)
        return configs

    def close(self, commit=True):
        if commit:
            self._cnx.commit()
        self._cnx.close()

    def execute(self, sql, params=None):
        self._cursor.execute(sql, params or (), multi=True)


if __name__ == '__main__':
    create_db = '''CREATE DATABASE ranker_db;'''
    db = Database()
    db.execute(create_db)

    create_table = '''
            USE ranker_db;
            CREATE TABLE `rankable_items` (
            `id` binary(32) NOT NULL DEFAULT '\\0\\0\\0\\0\\0\\0\\0\\0',
            `filename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
            `caption` varchar(100) DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        '''
    db.execute(create_table)

    db.close()


    # sql = '''
    #     INSERT INTO rankable_items(id, filename, caption)
    #     VALUES(UUID_TO_BIN(UUID()), %s, %s)
    # '''
    # values = ('test.png', 'hello there caption')
    # db.execute(sql, values)
    # db.close()
