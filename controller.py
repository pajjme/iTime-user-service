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
        
        #Generate a session key
        session_key = util.generate_random_session_key()
        
        #Create a new Session
        session = Session(session_key,account.id)
        
        try:
            #Store account 
            self.account_db_mapper.save(account)
            
            #Store session key 
            self.session_db_mapper.save(session)
            
            self.database.commit()
        except psycopg2.DatabaseError as error:
            if self.database.connection:
                self.database.rollback()
            print("Error:", error)
