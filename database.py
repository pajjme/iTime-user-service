import psycopg2

class Database:
    def __init__(self,host,database_name,user,password):
        self.db_name    = database_name
        self.host       = host
        self.user       = user
        self.password   = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(database=self.db_name,host=self.host,
                    port='5432',user=self.user)
            self.cursor = self.connection.cursor()
            return True
        except psycopg2.Error as error:
            print ("psycopg2 error: ", error)
            return False
    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def commit(self): 
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

