from databases.database import database
from models.bus_schema import Bus
from bson import ObjectId


async def bus_exists(bus_id:str):
    buses_collection = database.get_collection('buses')
    _id = ObjectId(bus_id)
    bus = await buses_collection.find_one(_id)
    
    if bus:
        return True
    return False

async def register_bus(bus_details:Bus):
    bus_collection = database.get_collection('buses')
    bus = await bus_collection.insert_one(bus_details.model_dump())
    print(bus.inserted_id)
    return bus.inserted_id

async def get_bus_id(student_id:str):
    users_collection = database.get_collection('users')
    student_object = ObjectId(student_id)

    student = await users_collection.find_one({'_id':student_object})
    bus_id = student['bus_id']
    return bus_id

async def get_bus_location(bus_id:str):
    bus_location_collection = database.get_collection('bus_location')
    
    return {}

