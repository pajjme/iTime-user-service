class AccountDatabaseMapper:

    def __init__(self,db):
        self.db = db

    def save(self,account):
        self.db.cursor.execute(
            "INSERT INTO accounts "+
            "(email,google_access_token,google_refresh_token) " +
            "VALUES (%s,%s,%s)",
            (account.email,account.access_token,account.refresh_token)
        )

        self.db.connection.commit()

