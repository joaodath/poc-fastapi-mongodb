import os
from dotenv import load_dotenv, find_dotenv

# needed to connect with mongodb
import motor.motor_asyncio

# needed to create the odmantic engine
from odmantic import AIOEngine

load_dotenv(find_dotenv())

motor_client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODBURI"])
engine = AIOEngine(motor_client=motor_client, database=os.environ["MONGODB"])

# database methods

# create


async def insert_one(data):
    """
    Inserts a new document into the database.
    The collection used is the one with the name matching the model name.

    Expects a dictionary with the data to be inserted.
    Returns the data inserted
    """
    try:
        result = await engine.insert_one(data)
        return result
    except Exception as e:
        print(e)
        return None


async def find_all(model):
    try:
        result = await engine.find(model= model)
        return result
    except Exception as e:
        print(e)
        return None


async def find_all_by_source(source):
    result = await engine.find({"source": source})
    return result


async def find_all_by_target(target):
    result = await engine.find({"target": target})
    return result


async def find_one_by_source(source):
    result = await engine.find_one({"source": source})
    return result


async def find_one_by_target(target):
    result = await engine.find_one({"target": target})
    return result

#exports the methods

if __name__ == "__main__":
    find_all()