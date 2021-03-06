from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SalaryGroup(BaseModel):
    title: str 
    basic_salary: float
    HRA: float
    MA: float

    class Config:
        orm_mode = True

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
    salary_group: SalaryGroup
    
    class Config:
        orm_mode = True

class EmployeeOut2(BaseEmployee):
    id: int
    created_at: Optional[datetime]
    active: bool
    
    class Config:
        orm_mode = True


    
