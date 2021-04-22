import datetime

import hashlib
from pytz import timezone

def createSession(*args):
    tempKeyWord = ''
    for arg in args:
        tempKeyWord += str(arg)
    tempKeyWord += str(datetime.datetime.now())
    password = tempKeyWord.encode('utf-8')
    key = hashlib.new('sha256')
    key.update(password)

    return key.hexdigest()


def nowDateTime(flag):
    KST = timezone('Asia/Seoul')
    if flag == 1:
        return datetime.datetime.utcnow()  #UTC
    elif flag == 2:
        return datetime.datetime.now(KST)

def get_timestamp(flag):
    return nowDateTime(flag).timestamp()