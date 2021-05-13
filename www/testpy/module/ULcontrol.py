import json, sys, os
from . import userLoginCheck, SuperAPIClass

class ULManager(SuperAPIClass.APIControlSys):
    ## SUB CLASS ##

    def get_apiname(self, data):
        self._data = data
        self._apiname = self._data['api']
        return self.getSeperateapi()

    def getSeperateapi(self):
    # Seperate by API Name
        if self._apiname == 'Login':         #login
            isdata = userLoginCheck.userLogin(self._data)
            result = json.dumps(isdata, indent=5)

        elif self._apiname == 'UserData':    #유저 info
            infodata = userLoginCheck.showUserInfo(self._data)
            result = json.dumps(infodata, indent=5)

        elif self._apiname == 'Time':        #utc, kst
            time_data = userLoginCheck.returnTimes(self._data)
            result = json.dumps(time_data, indent=5)

        elif self._apiname == 'test':
            result = json.dumps(self._data, indent=5)
        else:                               #API ERROR
            self._data.pop('reqdata')
            self._data.update({'retdata': 'Request api is {} ?'.format(self._apiname)})
            result = json.dumps(self._data, indent=5)

        return result



    



    