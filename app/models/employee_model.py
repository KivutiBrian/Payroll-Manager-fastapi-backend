from settings.db_setup import Base
from sqlalchemy import Column, Integer, String,Boolean,DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    surname = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    primary_phone_number = Column(String, nullable=False)
    secondary_phone_number = Column(String, nullable=False, default="N/A")
    email_address = Column(String, nullable=False)
    sgid = Column(Integer,ForeignKey('salary_groups.id'),nullable=False)
    created_at = Column(DateTime, default=func.now())
    active = Column(Boolean, default=True, nullable=False)

    salary_group = relationship('SalaryGroup', back_populates='employees')

    