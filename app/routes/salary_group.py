from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from settings.db_setup import get_db
from schemas.salary_group_schema import SalaryGroupCreate, SalaryGroupOut
from services.salarygroup_service import SalaryGroupService


router = APIRouter()

@router.get('',
summary='return a list of all salary groups',
response_model=List[SalaryGroupOut],
status_code = 200
)
async def salary_groups(db:Session = Depends(get_db)):
    return SalaryGroupService.salary_groups(db=db)

@router.get('/{sgid}',
summary='return a salary group by id',
response_model=SalaryGroupOut,
status_code = 200
)
async def find_group(sgid:int, db:Session = Depends(get_db)):
    return SalaryGroupService.get_salary_group(sgid=sgid, db=db)


@router.post('',
summary='create a new salary group',
response_model=SalaryGroupOut,
status_code=201
)
async def create_salary_group(payload:SalaryGroupCreate, db:Session = Depends(get_db)):
    return SalaryGroupService.add_salary_group(data=payload, db=db)

@router.put('/{sgid}',
summary='update a salary group',
response_model = SalaryGroupOut,
status_code=200
)
async def update_salary_group(sgid:int, db:Session = Depends(get_db)):
    return SalaryGroupService.update_salary_group(db=db)

@router.delete('/{sgid}',
summary='delete a salary group',
status_code=200
)
async def delete_salary_group(sgid:int, db:Session = Depends(get_db)):
    return SalaryGroupService.delete_salary_group(db=db)
