from flask import Flask, render_template, request
import os, sys, json

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from module import userLoginCheck, createNewSession, connectRedis
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# LOGIN, USERDATA, TIME API(POST)
@app.route('/UserWebAPI/ULManager', methods=['POST'])
def apistatus():
    try:
        R = connectRedis.RedisProject()
        userdata = request.get_json()
    except:
        result = json.dumps('Unknown JSON Type', indent=5)
        return result
    
    # Check NULL API, UID or Wrong API_VER
    if userdata['api'] or userdata['uid'] or (userdata['api_ver'] != 1):
        result = json.dumps(userdata, indent=5)
        return result
    
    seperate_api = userdata['api']

    # Seperate by API Name
    if seperate_api == 'Login':         #login
        isdata = userLoginCheck.userLogin(userdata)
        result = json.dumps(isdata, indent=5)

    elif seperate_api == 'UserData':    #유저 info
        infodata = userLoginCheck.showUserInfo(userdata)
        result = json.dumps(infodata, indent=5)

    elif seperate_api == 'Time':        #utc, kst
        time_data = userLoginCheck.returnTimes(userdata)
        result = json.dumps(time_data, indent=5)

    elif seperate_api == 'test':
        data = userdata
        result = json.dumps(data, indent=5)
    else:                               #API ERROR
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