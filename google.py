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

    #makes a new calender in google.
    def make_new_calendar(self):
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        calendar_body = {
            'summary' : 'iTime-Calendar-0001'
            'timeZone' : 'Europe/Stockholm'
        }
        self.calendar_Id = service.calendars().insert(body = calendar_body).execute()

