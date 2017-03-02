class Account:

    def __init__(self,id,email,access_token,refresh_token):
        self.id = id
        self.email = email
        self.access_token = access_token
        self.refresh_token = refresh_token
    
    def save(self,database):
        database.cursor.execute(
        "INSERT INTO accounts (email,google_access_token,google_refresh_token) VALUES (%s,%s,%s)",
        (self.email,self.access_token,self.refresh_token))

        database.connection.commit()


