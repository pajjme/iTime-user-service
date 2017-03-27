from database import Database
from account import Account
from account_db_mapper import AccountDatabaseMapper
from controller import Controller
from google import Google
import time
import sys
import os

def main():
    
    #fetch database credentials from env variables
    db_name = os.environ["ITIME_DB"]
    db_user = os.environ["ITIME_DB_USER"]
    db_password = os.environ["ITIME_DB_PASSWORD"]

    db = Database(db_name,db_user,db_password)
    i = 0
    #Try catch block
    while(not db.connect()):
        time.sleep(5)
        if(i >= 5):
            sys.exit()
        i += 1


    #fetch google client secret file path
    google_api_file = os.environ["ITIME_GOOGLE_API_FILE"]
    google = Google(google_api_file)

    #Temporary asking for auth code via stdin
    auth_code = input("auth code\n")

    controller = Controller(db,google)
    controller.new_account(auth_code)

    print("Exiting...")



if __name__ == '__main__':
    main()
