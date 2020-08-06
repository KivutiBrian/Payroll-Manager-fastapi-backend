from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from settings.db_setup import get_db
from schemas.salary_group_schema import SalaryGroupCreate, SalaryGroupOut


router = APIRouter()

@router.get('',
summary='return a list of all salary groups',
response_model=List[SalaryGroupOut],
status_code = 200
)
async def salary_groups(db:Session = Depends(get_db)):
    pass

@router.get('/{sgid}',
summary='return a salary group by id',
response_model=SalaryGroupOut,
salary_code = 200
)
async def find_group(sgid:int, db:Session = Depends(get_db)):
    pass

@router.post('',
summary='create a new salary group',
response_model=SalaryGroupOut,
status_code=201
)
async def create_salary_group(payload:SalaryGroupCreate, db:Session = Depends(get_db)):
    pass

