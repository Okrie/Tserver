import json
from . import dbSearchinsert, createNewSession, defineCode


def userLogin(userdata):
    ret = dbSearchinsert.isInData(userdata['uid'])   #데이터 있는지 판별
    reqdata = userdata['reqdata']
    if userdata['uid'] == -1:  # 신규유저
        registerNewUID()
    elif ret:   # 데이터 있으면
        reta = next(
            (item for item in dbSearchinsert.selectA('uid', userdata['uid'], 'session')
            if item['uid'] == int(userdata['uid'])), None)
        if reta['session'] == reqdata['session']:
            return defineCode.returnData(True, 'session', userdata, loginComplete(userdata, userdata['uid']))
        else:
            return defineCode.returnData(False, 'session', userdata, '')
    else:
        return 'None Data'

def registerNewUID():
    newUserdata = (dbSearchinsert.lastUid().get('uid')+1,1, createNewSession.createSession('uid'))   # 마지막 uid에 1 추가, 스테이지 1
    dbSearchinsert.insert(newUserdata)
    print('New Registered User')

def loginComplete(name, uid):
    init_key = createNewSession.createSession(name)
    dbSearchinsert.update(uid, '"' + init_key + '"')
    return init_key


# def testJsonReturn():   ##테스트 확인용
#     temp = dbSearchinsert.selectAllJson()   #Json형식으로 변경
#     temp2 = dbSearchinsert.jsonToLoad(temp)
#     temp3 = str(temp2[2]['session'])    #정보는 이런식으로 받아옴
#     print(temp2)
#     temp4 = dict(temp2[0])
#     return temp