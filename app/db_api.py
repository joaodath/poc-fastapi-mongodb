import os
from dotenv import load_dotenv, find_dotenv

#needed to connect with mongodb
import motor.motor_asyncio

load_dotenv(find_dotenv())


def get_database():
    #connection_string = f'mongodb://mongodb1:27017,mongodb2:27017,mongodb3:27017/?replicaSet=rsmongo'
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODBURI"])

    return client

if __name__ == "__main__":
    get_database()
