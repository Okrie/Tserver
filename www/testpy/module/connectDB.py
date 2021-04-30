import sys, pymysql, json
from . import defineCode
hostip = '192.168.244.129'
username = 'okrie'
pwd = '005605'
ondb = 'testdb'
encodingchar = 'utf8'
hostport = 3306

class DataBase():
    def __init__(self):
        try:
            self.connectdb = pymysql.connect(host=hostip, user=username, password=pwd, db=ondb, charset=encodingchar, port=hostport)
            self.cursor = self.connectdb.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            sys.exit(e)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def executeJsonAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = json.dumps(self.cursor.fetchall(), indent=5)
        return row

    def commit(self):
        self.connectdb.commit()