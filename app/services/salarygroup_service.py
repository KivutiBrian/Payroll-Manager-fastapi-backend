from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.salary_group_schema import SalaryGroupCreate
from models.salary_group_model import SalaryGroup

class SalaryGroupService:

    @staticmethod
    def salary_groups(db:Session):
        """return a list of all salary groups"""
        return db.query(SalaryGroup).all()

    @staticmethod
    def get_salary_group(sgid:int, db:Session):
        """"return a salary group  that matches the id"""
        record = db.query(SalaryGroup).filter(SalaryGroup.id == sgid).first()
        if not record:
            raise HTTPException(status_code=400, detail=f'no record matches id {sgid}')

        return record

    @staticmethod
    def add_salary_group(data:SalaryGroupCreate, db:Session):
        """create a new salary group"""
        record = SalaryGroup(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    @staticmethod
    def update_salary_group(db:Session):
        """üpdate salary group record"""
        pass

    @staticmethod
    def delete_salary_group(db:Session):
        """delete a salary group"""
        pass

