def get_database():
  import os
  from dotenv import load_dotenv, find_dotenv
  from pymongo import mongo_client
  import pymongo

  load_dotenv(find_dotenv())
  connection_string = f'mongodb://mongodb1:27017,mongodb2:27017,mongodb3:27017/{os.getenv("MONGODB")}?replicaSet=rsmongo'
  client = mongo_client.MongoClient(connection_string)

  return client

if __name__ == "__main__":
  mongodb = get_database()