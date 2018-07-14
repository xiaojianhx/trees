#/usr/bin/python3
# encoding: utf-8

import MySQLdb

class DBUtils:

    __conn = ''
    __cursor = ''

    def __init__(self):
        try:
            self.__conn = MySQLdb.connect('192.168.1.111', 'root', '123456', 'content', 3306, charset='utf8')
            self.__cursor = self.__conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as e:
            print (e)

    def save(self, sql, params):
        self.__cursor.execute(sql, params)

    def get(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

    def query(self, sql):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def commit(self):
        self.__conn.commit()

    def close(self):
        self.__cursor.close()
        self.__conn.close()