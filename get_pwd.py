import base64
import json
from sys import int_info
import pyperclip
from pwd_rec import *


class getPwd:

    def __init__(self,platform=None,id=None) -> None:
        self.platform = input("Platform:")

    def id_pwd(self,id,pwd):
        byt_obj = pwd[2:-1].encode('utf-8')
        dec_byt_obj = base64.b64decode(byt_obj)
        pwd = dec_byt_obj.decode()
        pyperclip.copy(pwd)
        print("Password for {} is copied to the clipboard".format(id))
        

    def get_pwd(self):
        
        with open("info",mode = 'r',encoding='utf-8-sig' )  as f:    
            if len(f.read()) == 0:
                print("No passwords entered yet")
                return
            else:
                f.seek(0)
                info_dict = json.load(f)
        
        if len(info_dict[self.platform]) == 0:
            print("No passwords for this platform yet")
        elif len(info_dict[self.platform]) == 1:
            rec = info_dict[self.platform][0]
            self.id_pwd(rec["id"],rec["pwd"])
        else:
            c = 1
            for  p in info_dict[self.platform]:
                print("{} for id : {}".format(c,p["id"]))
                c+=1   
            inp = int(input("Select the number of the id for which password is needed\n"))
            self.id_pwd(info_dict[self.platform][inp-1]["id"],info_dict[self.platform][inp-1]["pwd"])
        