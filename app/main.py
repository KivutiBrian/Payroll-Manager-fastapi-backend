from fastapi import FastAPI

#database setup
from settings.db_setup import Base, engine


app = FastAPI(
    title="Payroll System API",
    description="Backend for a payroll management system",
    redoc_url='/'
)

