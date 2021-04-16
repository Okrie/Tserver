import json
from . import dbSearchinsert, createNewSession


def userLogin(userdata):
    isOk = False
    ret = dbSearchinsert.isInData(userdata['uid'])   #데이터 있는지 판별
    if ret:
        reta = next(
            (item for item in dbSearchinsert.selectA('uid', userdata['uid'], 'session')
            if item['uid'] == int(userdata['uid'])), None)
        if reta['session'] == userdata['session']:
            loginComplete(userdata, userdata['uid'])
            return True
    else:
        return False


def registerNewUID():
    newUserdata = (dbSearchinsert.lastUid().get('uid')+1,1, createNewSession.createSession('uid'))   # 마지막 uid에 1 추가, 스테이지 1
    dbSearchinsert.insert(newUserdata)
    return 'New Registered User'

def loginComplete(name, uid):
    init_key = '"' + createNewSession.createSession(name) + '"'
    dbSearchinsert.update(uid, init_key)
    return 'User Login Success'

def testJsonReturn():   ##테스트 확인용
    temp = dbSearchinsert.selectAllJson()   #Json형식으로 변경
    temp2 = dbSearchinsert.jsonToLoad(temp)
    temp3 = str(temp2[2]['session'])    #정보는 이런식으로 받아옴
    print(temp2)
    temp4 = dict(temp2[0])
    return temp