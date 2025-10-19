from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

import os

load_dotenv()


connection_string = os.getenv('MONGO_CONNECTION_STRING')

client = AsyncIOMotorClient(connection_string)
database = client.bus_tracking



# database.create_collection('bus_location',check_exists=True)