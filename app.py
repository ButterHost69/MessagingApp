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

    if(opt == 2):
        if(login_obj.register() == 1):
            print(colored(" (+) User Created Successfully (+) " , "green"))
        
        elif(login_obj.register() == -1):
            print(colored(" (-) Incorrect Password !!! Please Try Again (-)" , "red"))
        
        else:
            print(colored(" (-) Some Internal Error Occurred (-)" , "red"))
    else:
        print(colored(" (-) Invalid Choice (-) " , "red"))
        os.system("pause")
        index()

def register():
    
    login_obj.registration()


index()