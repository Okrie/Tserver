import json
from . import createNewSession, defineCode, connectRedis, dbSearchinsert

# Login User with Redis
def userLogin(userdata):
    try:
        R = connectRedis.RedisProject()
        compressData = R.setKeyandValue(userdata)
        if userdata['uid'] == -1:   #신규유저
            newregist = registerNewUID()
            userdata['uid'] = newregist[0]
            reqdata = {'uid':userdata['uid']}
            reqdata.update({ compressData[1] : newregist[2]})
            R.updateRedis(reqdata)
            return defineCode.returnData(True, userdata, reqdata)

        reqdata = defineCode.requestDatas(userdata)
        ret = R.isInRedis(userdata)   #데이터 있는지 판별
        if ret:  # 데이터 있으면
            reta = R.searchInDBdata(userdata)
            print('uid = {0}, session = {1}, reqdata = {2}'.format(reta, reta['session'], reqdata['session']))
            if reta['session'] == reqdata['session']:   #키 대조
                strdata = {'session' : loginCompleteSession(userdata, userdata['uid'])}
                R.updateRedis(userdata)
                return defineCode.returnData(True, userdata, strdata)
            else:   #일치하지 않으면
                return defineCode.returnData(False, userdata, {'session':''})
        else:   # 없는 데이터
            return defineCode.returnData(False, userdata, {'session':'-100'})
    except Exception as e:
        print(e)
        return defineCode.returnData(False, userdata, {''})

# Show UserTable without KEY
def showUserInfo(userdata):
    try:
        ret = connectRedis.RedisProject().searchInDBdata(userdata)
        ret.pop('session')
        print(ret)
        return defineCode.returnData(True, userdata, ret)
    except Exception as e:
        print(e)
        return defineCode.returnData(False, userdata, {''})

# UTC, KST TimeStamp Return
def returnTimes(userdata):
    UTC_TIME = createNewSession.get_timestamp(1)
    KST_TIME = createNewSession.get_timestamp(2)
    time = {'UTC_TIME' : UTC_TIME, 'KST_TIME' : KST_TIME}
    return defineCode.returnData(True, userdata, time)

# Error Something
def somethingError(userdata, e):
    return json.dumps(defineCode.returnData(False, userdata, {e}), indent=5)

# Create New User
def registerNewUID():
    try:
        lastUid = dbSearchinsert.lastUid().get('uid') + 1
    except:
        lastUid = 1
    newUserdata = (lastUid,1, createNewSession.createSession('uid'))   # 마지막 uid에 1 추가, 스테이지 1, 세션 생성
    dbSearchinsert.insert(newUserdata)
    ret = dbSearchinsert.isInData(newUserdata[0])
    if ret:
        return newUserdata
    else:
        return False

# Create New KEY
def loginCompleteSession(name, uid):
    init_key = createNewSession.createSession(name)
    dbSearchinsert.update('session' ,uid, '"{}"'.format(init_key))
    return init_key

# If exists Redis, Connect Direct DB
def userLoginDB(userdata):
    try:
        reqdata = defineCode.requestDatas(userdata)
        for i in reqdata:
            strlist = i #키값

        if userdata['uid'] == -1:   #신규유저
            newregist = registerNewUID()
            userdata['uid'] = newregist[0]
            reqdata = { strlist : newregist[2]}
            reqdata.update({'uid':userdata['uid']})

        ret = connectRedis.isInRedis(userdata['uid'])   #데이터 있는지 판별

        if ret:  # 데이터 있으면
            reta = next(
                (item for item in dbSearchinsert.selectCondition('uid', userdata['uid'], 'session')
                if item['uid'] == int(userdata['uid'])), None)
            if reta['session'] == reqdata['session']:   #키 대조
                strdata = {'session' : loginCompleteSession(userdata, userdata['uid'])}
                return defineCode.returnData(True, userdata, strdata)
            else:                                       #일치하지 않으면
                return defineCode.returnData(False, userdata, {'session':''})
        else:   # 없는 데이터
            return defineCode.returnData(False, userdata, {'session':'-700'})
    except Exception as e:
        print(e)
        return defineCode.returnData(False, userdata, {''})


# def testJsonReturn():   ##테스트 확인용
#     temp = dbSearchinsert.selectAllJson()   #Json형식으로 변경
#     temp2 = dbSearchinsert.jsonToLoad(temp)
#     temp3 = str(temp2[2]['session'])    #정보는 이런식으로 받아옴
#     print(temp2)
#     temp4 = dict(temp2[0])
#     return temp