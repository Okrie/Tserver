from flask import Flask, render_template, request
import os, sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
#/home/okrie/var/www/testpy
from module import connectDB


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/send', methods=['GET', 'POST'])
def sendpostMSG():
    if request.method == 'GET':
        return render_template('post.html')
    elif request.method == 'POST':
        name = 'uid'
        nameValue = 'stage'

        dictdata = {'uid':int(request.form[name]),'stage':int(request.form[nameValue])}

        dbdata = selectAll()
        ret = next((item for item in dbdata if item[name] == int(request.form[name])), None)


        if ret[nameValue] == int(request.form[nameValue]):
            isOk = True
        else:
            isOk = False

        return render_template('default.html', result = isOk)


def selectAll():    #db 전부 검색
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users"
    row = db_class.executeAll(sql)
    return row


def select(name, uid):  #검색 조건
    db_class = connectDB.DataBase()
    sql = "SELECT * FROM users WHERE " + name + "=" + uid
    row = db_class.executeAll(sql)
    return row


def insert(uid):   #아직 작성중 0409
    db_class = connectDB.DataBase()
    sql = "INSERT INTO users VALUES " + uid + ""
    db_class.excute(sql)
    db_class.commit()
    return True



if __name__ == '__main__':
    app.run(debug=True)