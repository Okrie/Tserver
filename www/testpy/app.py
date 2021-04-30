from flask import Flask, render_template, request
import os, sys, json

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from module import userLoginCheck, createNewSession, connectRedis
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/UserWebAPI/ULManager', methods=['POST'])
def userloginCheck():
    try:
        userData = request.get_json()
        isdata = userLoginCheck.userLogin(userData)
        result = json.dumps(isdata, indent=5)
        if isdata['retmsg'] == 'SUCCESS':
            return result
        else:
            return result
    except:
        userData.pop('reqdata')
        userData.update({'retdata': '404'})
        return userData


####재설계를 위한 정리중####        uid, api Check => api -ing
@app.route('/UserWebAPI/ULManager/test', methods=['POST'])
def apistatus():
    try:
        userdata = request.get_json()
    except:
        result = json.dumps('Unknown JSON Type', indent=5)
        return result
    seperate_api = userdata['api']

    if userdata['api']:
        result = json.dumps(userdata, indent=5)

    if seperate_api == 'Login':         #login
        isTarget = connectRedis.RedisProject.uidCheck(userdata)
        if isTarget == 2:   #유저 uid 정보 없음
            print('is not have uid info')
            return userLoginCheck.somethingError(userdata)
        isdata = userLoginCheck.userLogin(isTarget, userdata)
        result = json.dumps(isdata, indent=5)
    elif seperate_api == 'UserData':    #유저 info
        infodata = userLoginCheck.showUserInfo(userdata)
        result = json.dumps(infodata, indent=5)

    elif seperate_api == 'Time':        #utc, kst
        time_data = userLoginCheck.returnTimes(userdata)
        result = json.dumps(time_data, indent=5)
    elif seperate_api == 'test':
        data = connectRedis
        result = json.dumps(data, indent=5)
    else:                               #ERROR
        userdata.pop('reqdata')
        userdata.update({'retdata': 'Request api is {} ?'.format(seperate_api)})
        result = json.dumps(userdata, indent=5)

    return result

if __name__ == '__main__':
    app.run(debug=True)

# api
# 1. 클라의 요청하는 데이터는 한곳에서 만든다
# 2. 클라가 요청해야하는 필수 Data 정의 하기
# 3. 1번에서 API에 맞게 분기해서 처리하기
# 4. 분기해서 처리된곳에서 리턴하기

#비교는 uid 받아와서 DB에서 검색 => 받은 Stage와 uid에 맞는 stage 비교 => 맞는지 아닌지 판단
# => 0413 완료
#데이터는 json 형태로 주고 받기
# -> 0414 완료
#접속시 session key 확인 및 새로운 세션키 생성 후 저장
# -> 0414 완료