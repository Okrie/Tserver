import sys, os

#sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from . import connectDB



## 아직 미완
class dbSearchInsert():        

    def selectAll(self):    #db 전부 검색
        self.db_class = connectDB.DataBase()
        sql = "SELECT * FROM users"
        row = self.db_class.executeAll(sql)
        return row


    def select(self, name, uid):  #검색 조건
        self.db_class = connectDB.DataBase()
        sql = "SELECT * FROM users WHERE " + name + "=" + uid
        row = self.db_class.executeAll(sql)
        return row


    def insert(self, uid):   #아직 작성중 0409
        self.db_class = connectDB.DataBase()
        sql = "INSERT INTO users VALUES " + uid + ""
        self.db_class.excute(sql)
        self.db_class.commit()
        return True
