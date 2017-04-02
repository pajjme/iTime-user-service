class AccountDatabaseMapper:

    def __init__(self,db):
        self.db = db

    def insert(self,account):
        self.db.cursor.execute(
            "INSERT INTO accounts "+
            "(google_id,email,google_access_token,google_refresh_token) " +
            "VALUES (%s,%s,%s,%s)",
            (account.id,account.email,account.access_token,account.refresh_token)
        )


