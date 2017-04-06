from database import Database
from account import Account
from account_db_mapper import AccountDatabaseMapper
from controller import Controller
from google import Google
from amqp_server import AmqpServer
import os
import time
import sys


def main():

    #fetch database credentials from env variables
    db_name = os.environ["ITIME_DB"]
    db_host = os.environ["ITIME_DB_HOST"]
    db_user = os.environ["ITIME_DB_USER"]
    db_password = os.environ["ITIME_DB_PASSWORD"]

    db = Database(db_host,db_name,db_user,db_password)
    connection_tries = 0

    #try to establish db connection, quit if it fails
    while(not db.connect()):
        print("Trying to reconnect to db,try starting postgres")
        time.sleep(5)
        if(connection_tries > 1):
            sys.exit(0)
        connection_tries+=1

    #fetch google client secret file path
    google_api_file = os.environ["ITIME_GOOGLE_API_FILE"]
    google = Google(google_api_file)

    controller = Controller(db,google)

    #Config for rabbitmq
    rabbit_server   = os.environ["ITIME_RABBIT_SERVER"]
    rabbit_queue    = os.environ["ITIME_RABBIT_US_QUEUE"]

    rabbit = AmqpServer(rabbit_server,rabbit_queue,controller.incoming)
    rabbit.start()
    print("Exiting...")

if __name__ == '__main__':
    main()
