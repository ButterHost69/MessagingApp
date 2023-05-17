from termcolor import *
import getpass
import json

AUTH_FILE_LOCATION = "files\\authfile.json"

class Users:
    def registration():

        username = input(colored(" [*] Username: " , "blue"))
        passwd = getpass.getpass(colored(" [*] Password: " , "blue"))
        confirmPass = getpass.getpass(colored(" [*] Confirm Password: " , "blue"))

        if(passwd == confirmPass):
            users = {
                "username" : username,
                "passwd" : passwd
            }
            
            
            with open(AUTH_FILE_LOCATION , "r") as file:
                data = json.load(file)
            
            data["users"].append(users)

            with open(AUTH_FILE_LOCATION , "w") as file:
                json.dump(data , file)
                return 1
                # print(colored(" (+) User Created Successfully (+) " , "green"))

        else:
            return -1
            # print(colored(" (-) Incorrect Password !!! Please Try Again (-)" , "red"))

