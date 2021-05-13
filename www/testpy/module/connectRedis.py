import redis
from . import dbSearchinsert, defineCode, createNewSession

REDIS_IP = '192.168.244.131'
REDIS_PORT = '6379'
#user = okrie
#pwd = 005605
#database = 'testdb'

####  mysql 처리와 비슷하지만 응답 받고 없으면 db요청 있으면 rtn 키값
class RedisProject():

    def __init__(self):
        try:
            self.rd = redis.StrictRedis(host=REDIS_IP, port=REDIS_PORT, db=0, charset='utf-8', decode_responses=True)
        except Exception as e:
            print(e)

    def searchInDBdata(self, userdata):  #정보 찾기
        try:
            getData = self.rd.get(userdata['uid'])
            print(getData)
            result = defineCode.setgetJsonType('get', getData)
            print(result)
            return result
        except Exception as e:
            print(e)
            return False
            

    def isInRedis(self, userdata):
        try:
            isindata = self.rd.get(userdata['uid']) #Redis 검색
            #print('isindata = {}'.format(isindata))
            if self.rd.exists(userdata['uid']) == 1:
                return True
            else:  ## redis에 데이터 없으면
                ret = dbSearchinsert.isInData(userdata['uid']) # db 검색
                if ret: # redis에 넣어야함 => set
                    dicts = dbSearchinsert.selectInfo('uid', userdata['uid'])
                    value = next((item for item in dicts if item['uid'] == userdata['uid']), None)
                    self.rd.set(userdata['uid'], defineCode.setgetJsonType('set', value))
                    #print('get data = {}'.format(self.rd.get(userdata['uid'])))
                    return True
                return False
        except Exception as e:
            print(e)

    def updateRedis(self, userdata):
        try:
            dicts = dbSearchinsert.selectInfo('uid', userdata['uid'])
            value = next((item for item in dicts if item['uid'] == userdata['uid']), None)
            self.rd.set(userdata['uid'], defineCode.setgetJsonType('set', value))
            print('Set Update')
            return True
        except Exception as e:
            print(e)

    def setKeyandValue(self, userdata): # 0 = value, 1 = reqdata
        reqdata = defineCode.requestDatas(userdata)
        print(reqdata)
        for i in reqdata:
            self._reqdata = i #키값
            self._req_val = reqdata[i]

        self._value = '{0}{1}'.format(self._reqdata, self._req_val)
        strRedisKeyValue = [self._value, self._reqdata]
        return strRedisKeyValue

    def uidCheck(self, userdata):     # 신규유저 인지 기존 유저인지 확인    #필요한가?
        if userdata['uid'] == -1:   # 신규유저
            return 0
        ret = self.rd.get(userdata['uid'])
        if ret:
            return 1    #기존 유저
        else:
            return 2    #없는 유저 정보

    def returncolumns(self):
        self.ret = dbSearchinsert.showColumns()
        return self.ret

    

