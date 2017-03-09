import json

class Account:

    def __init__(self,id,email,access_token,refresh_token):
        self.id = id
        self.email = email
        self.access_token = access_token
        self.refresh_token = refresh_token
    
    def get_json(self):
        dump = json.dumps(self.__dict__,sort_keys=True, indent=4)
        return dump

