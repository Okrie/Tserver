
HOSTIP = '192.168.244.129'
USERNAME = 'okrie'
PWD = '005605'
ONDB = 'testdb'
ENCODECHAR = 'utf8'
HOSTPORT = 3306

PYTHON_PATH = '/home/okrie/var/www/testpy/module'


# reqdata 부분만 받아서 처리하기    작성중
def requestDatas(reqdata):
    # require data
    data = reqdata['reqdata']
    return data


def returnData(booldata, userdata, returndata):
    # return data
    API = userdata['api']
    API_VERSION = userdata['api_ver']
    VER = userdata['ver']
    RETDATA = returndata
    if booldata:
        RETMSG = 'SUCCESS'
        responseTEXT = { 'api' : API, 'api_ver' : API_VERSION, 'ver' : VER, 'retmsg' : RETMSG, 'retdata' : RETDATA}
    else:
        RETMSG = 'FAIL'
        responseTEXT = { 'api' : API, 'api_ver' : API_VERSION, 'ver' : VER, 'retmsg' : RETMSG, 'retdata' : {}}
    return responseTEXT

def setDictionary(key, value):
    return { key : value }