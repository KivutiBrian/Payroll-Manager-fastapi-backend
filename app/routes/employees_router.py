from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from schemas.employee_schema import EmployeeOut,CreateEmployee
from schemas.user_schema import UserOut
from services.employee_service import EmployeeService
from settings.db_setup import get_db

from .auth import get_current_active_user

router = APIRouter()

@router.get('',
summary='return a list of all employees',
response_model = List[EmployeeOut],
response_description = "a list of all employees",
status_code=200
)
async def get_employees(db:Session = Depends(get_db), current_user: UserOut = Depends(get_current_active_user) ):
    return EmployeeService.read_employees(db=db)

@router.get('/{employee_id}',
summary='return a employee that matches the id',
response_model = EmployeeOut,
response_description = 'the employee'
)
async def employee_by_id(employee_id:int,db:Session = Depends(get_db), current_user: UserOut = Depends(get_current_active_user) ):
    return EmployeeService.read_employee_byID(employee_id=employee_id, db=db)

@router.post('',
summary="create new employee",
response_model=EmployeeOut,
response_description='the created employee'
)
async def create_employee(payload:CreateEmployee,db:Session = Depends(get_db), current_user: UserOut = Depends(get_current_active_user) ):
    return EmployeeService.create_employee(data=payload,db=db)

@router.put('',
summary="edit employee records",
response_model=EmployeeOut,
response_description='the created employee'
)
async def edit_employee(employee_id:int, db:Session=Depends(get_db), current_user: UserOut = Depends(get_current_active_user)):
    pass


@router.delete('',
summary="delete employee",
response_description='the created employee'
)
async def delete_employee(employee_id:int, db:Session=Depends(get_db), current_user: UserOut = Depends(get_current_active_user)):
    pass
