import httplib2
import datetime
from oauth2client import client
from apiclient import discovery

class Google:

    def __init__(self,client_secret_file):
        self.secret_file = client_secret_file
        
    
    def generate_oauth(self,auth_code):
        oauth = client.credentials_from_clientsecrets_and_code(self.secret_file,
                ['profile', 'email'],auth_code)

        self.credentials = oauth
    
    def get_access_token(self):
        return self.credentials.access_token
    
    def get_refresh_token(self):
        return self.credentials.refresh_token

    def get_email(self):
        return self.credentials.id_token['email']
    
    def get_id(self):
        return self.credentials.id_token['sub']