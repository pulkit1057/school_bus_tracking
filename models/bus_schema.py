from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Bus(BaseModel):
    bus_number:int
    number_plate:str
    driver_id:Optional[str] = None
    conductor_id:Optional[str] = None
    
    
class RouteDetails(BaseModel):
    bus_id:str
    longitude:float
    latitude:float
    
    
class MappingDetails(BaseModel):
    bus_id:str
    user_id:str
    
    
class AssignBusDetails(BaseModel):
    address:str
    user_id:str