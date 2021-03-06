import json
import util
import psycopg2
from account import Account
from session import Session
from account_db_mapper import AccountDatabaseMapper
from session_db_mapper import SessionDatabaseMapper
 
class Controller:

    def __init__(self,database,google):
        self.database = database
        self.google = google
        self.account_db_mapper = AccountDatabaseMapper(database)
        self.session_db_mapper = SessionDatabaseMapper(database)
    

    def incoming(self,body):
        #handles new rpc calls
        print(body)
        request_body = body.decode("utf-8")
        auth_code = json.loads(request_body)['auth_code']
        print(auth_code)


        try:
            
            id = self.new_account(auth_code)
            
            self.add_session_key(id)
            
            self.database.commit()
            
            return True
        except Exception as error:
            if self.database.connection:
                self.database.rollback()
            print("Error:", error) 

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
        self.account_db_mapper.insert(account)
        return account.id

    def add_session_key(self,google_id): 

        #Generate a session key
        session_key = util.generate_random_session_key()
        
        #Create a new Session
        session = Session(session_key,google_id)

        #Store session key 
        self.session_db_mapper.insert(session)
