import base64
import json
from account import Account
from account_db_mapper import AccountDatabaseMapper
class Controller:

    def __init__(self,database,google):
       self.database = database
       self.google = google
       self.account_db_mapper = AccountDatabaseMapper(database)


    def incoming(self,body):
        #handles new rpc calls
        print(body)
        request_body = body.decode("utf-8")
        auth_code = json.loads(request_body)['auth_code']
        print(auth_code)
        try:
           self.new_account(auth_code)
           return True
        except Exception as e:
            print(e)
            return False


    def new_account(self,auth_code):
        #call google to get new tokens
        self.google.generate_oauth(auth_code)

        access_token  = self.google.get_access_token()
        refresh_token = self.google.get_refresh_token()

        email = self.google.get_email()
        id = self.google.get_id()

        #Create a new account
        account = Account(id,
                        email,
                        access_token,
                        refresh_token)

        #Store account 
        self.account_db_mapper.save(account)
