from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime

from models.user_model import User
from schemas.user_schema import UserCreate


# create an obj to manage hashes and related configurations
pwd_content = CryptContext(schemes=['bcrypt'])


class UserService:

    @staticmethod
    def get_users(db:Session):
        """return a list of all users"""
        return db.query(User).all()

    @staticmethod
    def get_user_byID(user_id:int,db:Session):
        pass

    @staticmethod
    def create_user(payload:UserCreate, db:Session):
        
        # check if email exists
        user_email = db.query(User).filter(User.email == payload.email).first()
        if user_email:
            raise HTTPException(status_code=400, detail='Email already in use')
        
        # check if username exists
        username = db.query(User).filter(User.username == payload.username).first()
        if username:
            raise HTTPException(status_code=400, detail='Username already in user')
        
        # add record to database
        record = User(username=payload.username,email=payload.email,first_name=payload.first_name,last_name=payload.last_name,
                        password=pwd_content.hash(payload.password))
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
        