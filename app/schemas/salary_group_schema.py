from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from schemas.employee_schema import EmployeeOut

class SalaryGroupBase(BaseModel):
    title: str
    basic_salary: float
    HRA: float
    MA: float

class SalaryGroupCreate(SalaryGroupBase):
    pass

class SalaryGroupOut(SalaryGroupBase):
    id: int
    created_at: Optional[datetime]
    employees: List[EmployeeOut] = []

    class Config:
        orm_mode = True