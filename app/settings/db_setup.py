from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URi = 'sqlite:///PayrollDataBase'

# core interface to the database
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread":False}, echo=False)

# talk to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# class to describe the database
Base = declarative_base()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()