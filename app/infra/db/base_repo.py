import mysql.connector
import json
import re
from typing import Union
import os

class BaseRepo:
    def __init__(self):
        self.HOST = os.environ['DB_HOST']
        self.PORT = os.environ['DB_PORT']
        self.DATABASE = os.environ['DB_DATABASE']
        self.USERNAME = os.environ['DB_USERNAME']
        self.PASSWORD = os.environ['DB_PASSWORD']
    
        self._conn = self._connect()
        self._cur = self._create_cursor()

    def _connect(self):
        conn = mysql.connector.connect(
            user=self.USERNAME,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            database=self.DATABASE,
            autocommit=False)
        return conn

    def _create_cursor(self):
        cursor = self._conn.cursor(dictionary=True)
        return cursor

    def execute(self, sql, params: dict = None):
        """SQLを実行する.

        Args:
            conn ([type]): [description]
            cur ([type]): [description]
            sql ([type]): [description]
            params ([dict], optional): [description]
        """
        sql = sql.replace('\n', '')
        sql = re.sub(r'\s+', ' ', sql)

        self._cur.execute(sql, params)

    def fetchall(self):
        return self._cur.fetchall()

    def commit(self):
        self._conn.commit()

    def exception_handler(self, error: Exception):
        self._conn.rollback()

    def clean_up(self):
        if self._cur is not None:
            self._cur.close()
        if self._conn is not None:
            self._conn.close()
        return
