from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime



class BaseEmployee(BaseModel):
    surname: str
    first_name: str
    last_name: str
    primary_phone_number: str
    secondary_phone_number: str
    email_address: str

    

class CreateEmployee(BaseEmployee):
    sgid: int


class EmployeeOut(BaseEmployee):
    id: int
    created_at: Optional[datetime]
    active: bool
    

    class Config:
        orm_mode = True

    
