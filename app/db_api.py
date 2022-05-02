def get_database():
  from pymongo import mongo_client
  import pymongo

  connection_string = "mongodb://mongodb1:27017"
  client = mongo_client.MongoClient(connection_string)

  return client

if __name__ == "__main__":
  mongodb = get_database()