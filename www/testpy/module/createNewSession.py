import datetime
import hashlib

def createSession(*args):
    tempKeyWord = ''
    for arg in args:
        tempKeyWord += str(arg)
    tempKeyWord += str(datetime.datetime.now())
    password = tempKeyWord.encode('utf-8')
    key = hashlib.new('sha256')
    key.update(password)

    return key.hexdigest()


def nowDateTiem():
    return str(datetime.datetime.now())