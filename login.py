from termcolor import *
import getpass
import firebase_admin
import os
import json
import requests
import pprint

from firebase_admin import credentials
from firebase_admin import auth

# Firebase Personel Authentication Key
FIREBASE_REST_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
SERVICE_ACCOUNT_FILE = "__keys__\chatapp-903c2-firebase-adminsdk-2hnxc-aa594f1e3e.json"
FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")

cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)

# Initializing Firebase
firebase_admin.initialize_app(cred)

class Users:
    def registration():
              
        email = input(colored(" [*] Email : " , "blue"))
        passwd = getpass.getpass(colored(" [*] Password [ (6) letters or more ] : " , "blue"))
        confirmPass = getpass.getpass(colored(" [*] Confirm Password : " , "blue"))

        if(passwd == confirmPass):

            try:
                user = auth.create_user(email= email , password= passwd)            

                print(user)
                return 1
                print(colored(" (+) User Created Successfully (+) " , "green"))
            
            except :

                print(user)
                return 0
                print(colored(" (-) Email Already Exists (-) " , "red"))
                

        else:

            return -1
            print(colored(" (-) Incorrect Password !!! Please Try Again (-)" , "red"))

    def login():

        email = input(colored(" [*] Email : " , "blue"))
        passwd = getpass.getpass(colored(" [*] Password : " , "blue"))
        
        # initialize firebase auth
        credential = json.dumps(
            {
                "email" : email,
                "password" : passwd
            }
        )

        r = requests.post(
            FIREBASE_REST_URL,
            params={"key" : FIREBASE_WEB_API_KEY},
            data=credential
        )

        loginJsonString = r.json()
        # check for if login true
        
        #ifError = r['error'][0]['message']
        if "error" in loginJsonString:
            print(colored(" (-) Incorrect Email/Passwd (-) " , "red"))
        else:
            print(colored(" (+) Logged In Successfully (+) " , "green"))

            
            
     

