import os 
import sys
import base64
from pwd_rec import *
import json


class putPwd():

    def __init__(self):
        self.platform = input("Platform:")
        self.id = input("Id:")
        self.pwd = input("Password:")


    def put_pwd(self):
        
        with open("info",mode = 'r',encoding='utf-8-sig' )  as f:    
            if len(f.read()) == 0:
                info_dict = {}
            else:
                f.seek(0)
                info_dict = json.load(f)

        rec_obj = PwdRec(**self.__dict__)
        rec_obj.pwd =  str(base64.b64encode(rec_obj.pwd.encode('utf-8')))
        
        if rec_obj.platform in info_dict.keys():
            print(type(info_dict[rec_obj.platform]))
            inner_lst = info_dict[rec_obj.platform]
            inner_dict = {"id":rec_obj.id,"pwd":rec_obj.pwd}
            inner_lst.append(inner_dict)
        else:
            info_dict[rec_obj.platform] = [{"id":rec_obj.id,"pwd":rec_obj.pwd}]
        
        with open("info","w") as f:
            f.write(json.dumps(info_dict,indent=4))
        
    

            
