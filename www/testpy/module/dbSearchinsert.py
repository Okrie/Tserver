import json
from . import connectDB

def selectAll():    #db 전부 검색
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users"
    row = db_class.executeAll(sql)
    return row

def showColumns():
    db_class = connectDB.DataBase()
    #sql = "SHOW COLUMNS FROM users"
    sql = "SELECT COLUMN_NAME as 'Field' FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'users'"
    row = db_class.executeAll(sql)
    return row

def selectAllJson():    #db => json
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users"
    row = db_class.executeJsonAll(sql)
    return row

def jsonToLoad(data_json):
    data = json.loads(data_json)
    return data

def select(name, value):  #검색 조건
    db_class = connectDB.DataBase()
    sql = "SELECT {0} FROM users WHERE {0} = {1}".format(name, value)
    row = db_class.executeAll(sql)
    return row

def selectInfo(name, value):    #유저 정보
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users WHERE {0} = {1}".format(name, value)
    row = db_class.executeAll(sql)
    return row

def selectCondition(name, value, condition):  #특정 검색 조건
    db_class = connectDB.DataBase()
    sql = "SELECT {0}, {1} FROM users WHERE {0} = {2}".format(name, condition, value)
    row = db_class.executeAll(sql)
    return row

def insert(newUser):    #신규 유저 추가
    db_class = connectDB.DataBase()
    sql = "INSERT INTO users VALUES {}".format(newUser)
    db_class.execute(sql)
    db_class.commit()
    return True

def insertS(_userSession):   #세션
    db_class = connectDB.DataBase()
    sql = "INSERT INTO users(uid, session) VALUES {}".format(_userSession)
    db_class.execute(sql)
    db_class.commit()
    return True

def update(name, value, key):     #신규 정보로 저장
    db_class = connectDB.DataBase()
    sql = "UPDATE users set {0} = {2} WHERE uid = {1}".format(name, value, key)
    db_class.executeAll(sql)
    db_class.commit()
    return True

def lastUid():      #UID 마지막 값 찾기
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users ORDER BY uid DESC LIMIT 1"
    row = db_class.executeOne(sql)
    return row

def isInData(uid):
    db_class = connectDB.DataBase()
    sql = "SELECT uid FROM users WHERE uid = {}".format(uid)
    row = db_class.executeAll(sql)
    if row: #데이터 있을때
        return True
    else:   #데이터 없음
        return False
