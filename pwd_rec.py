
from sys import platform
import json

class PwdRec():

    def __init__(self,platform = None,id = None,pwd = None, **kwargs):
            self.platform = platform
            self.pwd = pwd
            self.id = id 

    def get_rec(self):
        model_dict = {self.platform: [{"id":self.id,"pwd":self.pwd}] }
        print(model_dict)
        return json.dumps(model_dict) 


        