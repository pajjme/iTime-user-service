class SessionDatabaseMapper:

    def __init__(self,db):
        self.db = db

    def insert(self,session):
        self.db.cursor.execute(
            "INSERT INTO sessions "+
            "(session,google_id) " +
            "VALUES (%s,%s)",
            (session.key,session.google_id)
        )

