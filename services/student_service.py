from databases.database import database
from models.student_schema import Student
from models.bus_schema import MappingDetails
from bson import ObjectId

async def create_student(student:Student):
    users_collection = database.get_collection('users')
    new_student = await users_collection.insert_one(student.model_dump())
    return str(new_student.inserted_id)

async def get_student(student_id:str):
    users_collection = database.get_collection('users')
    _id = ObjectId(student_id)
    student = await users_collection.find_one({"_id":_id})
    student["_id"] = str(student["_id"])
    return student

async def user_exists(user_id:str):
    users_collection = database.get_collection('users')
    _id = ObjectId(user_id)
    student = await users_collection.find_one(_id)
    
    if student:
        return True
    return False

async def assign_bus_to_user(mapping_details:MappingDetails):
    student_bus_mapping_collection = database.get_collection('student_bus_mapping')
    new_mapping = student_bus_mapping_collection.insert_one(mapping_details.model_dump())
    return new_mapping


async def bus_already_assigned(user_id:str):
    student_bus_mapping_collection = database.get_collection('student_bus_mapping')
    student = await student_bus_mapping_collection.find_one({'user_id':user_id})
    
    if student:
        return True
    return False