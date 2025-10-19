from pydantic import BaseModel
from typing import Optional

class Bus(BaseModel):
    bus_number:int
    number_plate:str
    driver_id:Optional[str] = None
    conductor_id:Optional[str] = None