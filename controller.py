from account import Account
from account_db_mapper import AccountDatabaseMapper
class Controller:

    def __init__(self,database,google):
       self.database = database
       self.google = google
       self.acc_db_mapper = AccountDatabaseMapper(database)


    def new_account(self,auth_code):
        #call google object to get new tokens
        self.google.generate_oauth(auth_code)


        access_tok  = self.google.get_access_token()
        refresh_tok = self.google.get_refresh_token()
        email = self.google.get_email()
        id = self.google.get_id()
        #create a new account, supplying email + tokens
        account = Account(id,
                        email,
                        access_tok,
                        refresh_tok)

        #store a account inject the database
        self.acc_db_mapper.save(account)
        print("Creating account in db")
