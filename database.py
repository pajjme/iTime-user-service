import psycopg2

class Database:
    def __init__(self,database_name,user,password):
        self.db_name    = database_name
        self.user       = user
        self.password   = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect("dbname="+self.db_name+" user="+self.user)
            self.cursor = self.connection.cursor()
            return True
        except psycopg2.Error as error:
            print ("psycopg2 error: ", error)
            return False
        

    def disconnect():
        self.cursor.close()
        self.connection.close()
