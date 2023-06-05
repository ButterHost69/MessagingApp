from termcolor import colored
import os

from login import *

# For Login And Register Functions
login_obj = Users 

def index():
    os.system("cls")

    print(colored("      Chapri CHATS " , "white"))
    print(colored("--------------------------" , "yellow"))
    print(colored(" [1] Login " , "cyan"))
    print(colored(" [2] Register " , "cyan"))
    print(colored("--------------------------" , "yellow"))
    opt = int(input(" "))
    
    if(opt == 1):
        login_obj.login()

    elif(opt == 2):
        regAcc = 0
         
        while(regAcc != 1):
            regAcc =  register()
        
    else:
        print(colored(" (-) Invalid Choice (-) " , "red"))
        os.system("pause")
        index()


def register():
    accountCreate = login_obj.registration()

    if(accountCreate == 1):
        print(colored(" (+) User Created Successfully (+) " , "green"))
        os.system("pause")
        return 1
        
    elif(accountCreate == 0):
        print(colored(" (-) Email Already Exists (-)" , "red"))
    
    elif(login_obj.registration == -1):
        print(colored(" (-) Password Does Not Match (-)" , "red"))
    
    else:
        print(colored(" (-) Some Internal Error Occurred (-)" , "red"))

    os.system("pause")
    return 0


def login():
    auth = login_obj.login()
    if(auth == 1):
        print(colored(" (+) Logged In Successfully (+)" , "green"))
        os.system("pause")
        return 1
        
    elif(auth == 0):
        print(colored(" (-) Incorrect Username/Password (-)" , "red"))
        
    
    else:
        print(colored(" (-) Some Error Occured (-)" , "red"))

    os.system("pause")
    return 0

index()