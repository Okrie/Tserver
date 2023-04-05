import pymysql



class DataBase():
    def __init__(self):
        hostip = '192.168.244.129'
        self.connectdb = pymysql.connect(host=hostip, user='******', password='******', db='testdb', charset='utf8', port=****)
        self.cursor = self.connectdb.cursor(pymysql.cursors.DictCursor)
        #pymysql.cursors.DictCursor

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

    def commit(self):
        self.connectdb.commit()
