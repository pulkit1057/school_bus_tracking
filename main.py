from fastapi import FastAPI, HTTPException
import os
from services.student_service import create_student, get_student, user_exists, assign_bus_to_user, bus_already_assigned
from services.bus_service import get_bus_id, get_bus_location, register_bus, bus_exists
from models.student_schema import Student
from models.bus_schema import Bus, RouteDetails, MappingDetails, AssignBusDetails

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


@app.post('/assign-bus-stop/')
async def assign_bus_stop(assign_stop_details:AssignBusDetails):
    coordinates = await get_geocode(assign_stop_details.address)
    pass


@app.post('/assign-bus/')
async def assign_bus(mapping_details:MappingDetails):
    
    if await user_exists(mapping_details.user_id) == False:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if await bus_exists(mapping_details.bus_id) == False:
        raise HTTPException(status_code=404, detail="Bus not found")
    
    if await bus_already_assigned(mapping_details.user_id):
        raise HTTPException(status_code=404,detail="User already been allotted with a bus")
    
    await assign_bus_to_user(mapping_details)
    
    return {"message":"Assigned a bus successfully"}


@app.get('get-location/{student_id}')
async def get_location(student_id:str):
    bus_id = get_bus_id(student_id)
    bus_coordinates = get_bus_location(bus_id)
    return bus_coordinates




@app.post('update-bus-coordinates/{bus_id}')
async def update_bus_coordinates():
    return {}





@app.post('/assign-route-to-bus/')
async def assign_route(route_details:RouteDetails):
    
    return {}