from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SalaryGroupBase(BaseModel):
    title: str
    basic_salary: float
    HRA: float
    HA: float

class SalaryGroupCreate(SalaryGroupBase):
    pass

class SalaryGroupOut(SalaryGroupBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True