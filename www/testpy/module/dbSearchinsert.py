import json
from . import connectDB

def selectAll():    #db 전부 검색
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users"
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
    sql = "SELECT " + name + " FROM users WHERE " + name + "=" + value
    row = db_class.executeAll(sql)
    return row

def selectCondition(name, value, condition):  #특정 검색 조건
    db_class = connectDB.DataBase()
    sql = "SELECT " + name + "," + condition + " FROM users WHERE " + name + "=" + str(value)
    row = db_class.executeAll(sql)
    return row

def insert(newUser):    #신규 유저 추가
    db_class = connectDB.DataBase()
    sql = "INSERT INTO users VALUES " + str(newUser)
    db_class.execute(sql)
    db_class.commit()
    return True

def insertS(_userSession):   #세션
    db_class = connectDB.DataBase()
    sql = "INSERT INTO users(uid, session) VALUES " + _userSession
    db_class.execute(sql)
    db_class.commit()
    return True

def update(value, key):     #신규 키로 저장
    db_class = connectDB.DataBase()
    sql = "UPDATE users set session = " + key + " WHERE uid = " + str(value)
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
    sql = "SELECT uid FROM users WHERE uid =" + str(uid)
    row = db_class.executeAll(sql)
    if row: #데이터 있을때
        return True
    else:   #데이터 없음
        return False
