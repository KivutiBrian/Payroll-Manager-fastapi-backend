from settings.db_setup import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy import func
from sqlalchemy.orm import relationship

class SalaryGroup(Base):
    __tablename__ = 'salary_groups'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    basic_salary = Column(String, nullable=False)
    HRA = Column(Float, nullable=False) #House Rent Allowance
    MA = Column(Float, nullable=False) #Medical Allowance
    created_at = Column(DateTime, default=func.now(), nullable=False)

    employees = relationship('Employee', backref='salary_group', lazy=True)




