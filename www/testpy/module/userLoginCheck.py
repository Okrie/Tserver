import json
from . import dbSearchinsert, createNewSession, defineCode


def userLogin(flag, userdata):
    try:
        if flag == 0:   #신규유저
            newregist = registerNewUID()
            userdata['uid'] = newregist[0]
            userdata['reqdata'] = {'session' : newregist[2]}        
        ret = dbSearchinsert.isInData(userdata['uid'])   #데이터 있는지 판별
        reqdata = userdata['reqdata']
        if ret:  # 데이터 있으면
            reta = next(
                (item for item in dbSearchinsert.selectCondition('uid', userdata['uid'], 'session')
                if item['uid'] == int(userdata['uid'])), None)
            if reta['session'] == reqdata['session']:   #키 대조
                strdata = {'session' : loginCompleteSession(userdata, userdata['uid'])}
                if flag == 0 :
                    strdata.update({'uid':userdata['uid']})
                return defineCode.returnData(True, userdata, strdata)
            else:                                       #일치하지 않으면
                return defineCode.returnData(False, userdata, {'session':''})
        else:   # 없는 데이터
            return defineCode.returnData(False, userdata, {'session':'-700'})
    except:
        return defineCode.returnData(False, userdata, {''})

def uidCheck(userdata):     # 신규유저 인지 기존 유저인지 확인
    if userdata['uid'] == -1:   # 신규유저
        return 0
    ret = dbSearchinsert.isInData(userdata['uid'])
    if ret:
        return 1    #기존 유저
    else:
        return 2    #없는 유저 정보

def returnTimes(userdata):  # UTC, KST
    UTC_TIME = createNewSession.get_timestamp(1)
    KST_TIME = createNewSession.get_timestamp(2)
    time = {'UTC_TIME' : UTC_TIME, 'KST_TIME' : KST_TIME}
    return defineCode.returnData(True, userdata, time)

def somethingError(userdata):   # 무언가 에러
    return json.dumps(defineCode.returnData(False, userdata, {''}), indent=5)

def registerNewUID():   #신규 유저 등록
    newUserdata = (dbSearchinsert.lastUid().get('uid')+1,1, createNewSession.createSession('uid'))   # 마지막 uid에 1 추가, 스테이지 1, 세션 생성
    dbSearchinsert.insert(newUserdata)
    ret = dbSearchinsert.isInData(newUserdata[0])
    if ret:
        return newUserdata
    else:
        return False

def loginCompleteSession(name, uid):
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