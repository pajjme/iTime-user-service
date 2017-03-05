import psycopg2

class Database:
    def __init__(self,database_name,user,password):
        self.db_name    = database_name
        self.user       = user
        self.password   = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect("dbname="+self.db_name+" user="+self.user)
        self.cursor = self.connection.cursor()

    def disconnect():
        self.cursor.close()
        self.connection.close()
