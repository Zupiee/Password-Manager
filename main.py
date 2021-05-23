
from get_pwd import *
from put_pwd import *


def main():
    print("########################################")
    inp = input("G or g to get pwd \n p or P to put pwd\n Any other key to exit\n")
    if inp in ["G","g"]:
        get_obj = getPwd()
        get_obj.get_pwd()
    elif inp in ["p","P"]:
        put_obj = putPwd()
        put_obj.put_pwd() 
    elif inp in ["Q","q"]:
        exit()
    else:
        print("Wrong input")
        
if __name__ == "__main__":
    while(True):
        main()

