from databases.database import database
from models.student_schema import Student
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