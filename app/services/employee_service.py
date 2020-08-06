from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.employee_model import Employee
from schemas.employee_schema import CreateEmployee

class EmployeeService:

    @staticmethod
    def read_employees(db:Session):
        """return a list of all employees from the database """
        return db.query(Employee).all()

    @staticmethod
    def read_employee_byID(employee_id:int, db:Session):
        """return a employee that matches emplyee_id"""
        record = db.query(Employee).filter(Employee.id == employee_id).first()
        if not record:
            raise HTTPException(status_code=400, details=f'No record with employee_id {employee_id}')

        return record

    @staticmethod
    def create_employee(data:CreateEmployee, db:Session):
        """create a new employee"""
        email = db.query(Employee).filter(Employee.email==data.email).first()
        if email:
            raise HTTPException(status_code=400, detail='email taken!')
        
        # save to database
        record = Employee(**data.dict())
        db.add(record)
        db.commit()
        db.refresh()
        return record


    @staticmethod
    def update_employee_record(data,employee_id:int, db:Session):
        """update employee record"""
        record = db.query(Employee).filter(Employee.id == employee_id ).first()
        if not record:
            raise HTTPException(status_code=400, detail='No record matches the id provided')

    @staticmethod
    def deactivate_employee(employee_id:int, db:Session):
        """deactivate an employee"""
        record = db.query(Employee).filter(Employee.id == employee_id ).first()
        if not record:
            raise HTTPException(status_code=400, detail='No record matches the id provided')
        # set the active status to false
        record.active = False
        db.commit()
        return record