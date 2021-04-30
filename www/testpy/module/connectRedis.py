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
        self.rd = redis.StrictRedis(host=REDIS_IP, port=REDIS_PORT, db=0)

    def searchInDBdata(self, indata):  #정보 찾기
        #strisIndata = '{0}{1}'.format('uid', userdata['uid'])
        #isindata = self.rd.get(strisIndata)
        #defineCode.requestDatas(userdata)
        isBooldata = isInRedis(indata)
        if isBooldata:
            result = self.rd.get(indata['uid'])
        else:
            return indata

        return result

    def isInRedis(self, userdata):
        isindata = self.rd.get(userdata['uid']) #Redis 검색
        ret = dbSearchinsert.isInData(userdata['uid']) # db 검색
        if isindata:
            return True
        elif ret:
            return True
        else:   ## redis에 데이터 없으면
            return False

    

    def uidCheck(self, userdata):     # 신규유저 인지 기존 유저인지 확인
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

    

