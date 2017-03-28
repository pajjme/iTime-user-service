from database import Database
from account import Account
from account_db_mapper import AccountDatabaseMapper
from controller import Controller
from google import Google
from amqp_server import AmqpServer
import os


def main():
    
    test = 4/0
    #fetch database credentials from env variables
    db_name = os.environ["ITIME_DB"]
    db_user = os.environ["ITIME_DB_USER"]
    db_password = os.environ["ITIME_DB_PASSWORD"]

    db = Database(db_name,db_user,db_password)
    db.connect()

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
