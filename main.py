from fastapi import FastAPI, HTTPException
import os
from services.student_service import create_student, get_student
from services.bus_service import get_bus_id, get_bus_location, register_bus
from models.student_schema import Student
from models.bus_schema import Bus

app = FastAPI()

@app.get('/')
def root():
    return {"Hello":"World"}



@app.post('/register-user/')
async def register_user(student_details:Student):
    new_student = await create_student(student_details)
    return {"message":"Student created successfully","student_id":new_student,}



@app.post('/register-bus/')
async def create_bus(bus_details:Bus):
    new_bus = await register_bus(bus_details)
    bus_id = str(new_bus)
    return {"message":"Bus registered successfully","bus_id":bus_id,}




@app.get('/user-info/{student_id}')
async def user_info(student_id:str):
    student_details = await get_student(student_id) 
    if student_details:
        return student_details
    raise HTTPException(status_code=404, detail="Student not found")



@app.post('/assign-bus/')
async def assign_bus():
    return {}


@app.get('get-location/{student_id}')
async def get_location(student_id:str):
    bus_id = get_bus_id(student_id)
    bus_coordinates = get_bus_location(bus_id)
    return bus_coordinates




@app.post('update-bus-coordinates/{bus_id}')
async def update_bus_coordinates():
    return {}