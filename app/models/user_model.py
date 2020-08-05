from settings.db_setup import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class UserModel(Base):
    id = Column(Integer, primary_key=True)