from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int
    address:str
    roll_no:int
    email:str