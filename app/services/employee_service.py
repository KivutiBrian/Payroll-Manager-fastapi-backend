from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.employee_model import Employee

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
    def create_employee(data, db:Session):
        """create a new employee"""
        pass

    @staticmethod
    def update_employee_record(data,employee_id:int, db:Session):
        """update employee record"""
        pass

    @staticmethod
    def deactivate_employee(employee_id:int, db:Session):
        """deactivate an employee"""
        pass
