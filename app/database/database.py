import os
from dotenv import load_dotenv, find_dotenv
from bson import ObjectId

# needed to connect with mongodb
import motor.motor_asyncio

# needed to create the odmantic engine
from odmantic import AIOEngine

load_dotenv(find_dotenv())

# creating engine
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
        result = await engine.save(data)
        return result
    except Exception as e:
        print(e)
        return None


async def find_all(model):
    try:
        result = await engine.find(model=model)
        return result
    except Exception as e:
        print(e)
        return None


async def find_one_by_id(model, id):
    try:
        result = await engine.find_one(model, model.id == ObjectId(id))
        return result
    except Exception as e:
        print(e)
        return None
