from database import Database
from account import Account
from account_db_mapper import AccountDatabaseMapper
import os

def main():
    #fetch database credentials from env variables
    db_name = os.environ["ITIME_DB"]
    db_user = os.environ["ITIME_DB_USER"]
    db_password = os.environ["ITIME_DB_PASSWORD"]
    db = Database(db_name,db_user,db_password)
    db.connect()

    account_db_mapper = AccountDatabaseMapper(db)


    account = Account(0,"herpa@derpa.com","123","30")

    account_db_mapper.save(account)
    print("Exiting...")



if __name__ == '__main__':
    main()
