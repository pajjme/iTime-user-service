from database import Database
from account import Account
from account_db_mapper import AccountDatabaseMapper
from controller import Controller
from google import Google
import os

def main():
    
    #fetch database credentials from env variables
    db_name = os.environ["ITIME_DB"]
    db_user = os.environ["ITIME_DB_USER"]
    db_password = os.environ["ITIME_DB_PASSWORD"]

    db = Database(db_name,db_user,db_password)
    db.connect()

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
