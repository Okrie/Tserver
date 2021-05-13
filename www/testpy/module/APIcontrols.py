from . import ULcontrol, defineCode

class APISeperate():
    ### Seperate API ###

    def __init__(self):
        self.U = ULcontrol.ULManager()

    def setData(self, data, api_name):
        self._data = data
        self._apiname = api_name
        return self.seperateApi()

    def seperateApi(self):
        if self._apiname == 'ULManager':
            return self.U.get_apiname(self._data)
        else:
            return defineCode.returnData(False, self._data, self._apiname)
