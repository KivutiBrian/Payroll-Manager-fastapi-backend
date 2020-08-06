from fastapi import FastAPI

#database setup
from settings.db_setup import Base, engine
from models.user_model import User
from models.employee_model import Employee
from models.salary_group_model import SalaryGroup
Base.metadata.create_all(bind=engine)

# routes imports
from routes import users_router, employees_router, salary_group

app = FastAPI(
    title="Payroll System API",
    description="Backend for a payroll management system",
    redoc_url='/'
)

# register all routes
app.include_router(
    users_router.router,
    prefix='/users',
    tags=['Users Operations'],
    responses={200:{'description':'Ok'}, 201:{'description':'Created'}, 400:{'description':'Bad Request'}, 401:{'desription':'Unauthorized'}}
)

app.include_router(
    salary_group.router,
    prefix='/salary-groups',
    tags=['Salary Group Operations'],
    responses={200:{'description':'Ok'}, 201:{'description':'Created'}, 400:{'description':'Bad Request'}, 401:{'desription':'Unauthorized'}}
)


app.include_router(
    employees_router.router,
    prefix='/employees',
    tags=['Émployees Operations'],
    responses={200:{'description':'Ok'}, 201:{'description':'Created'}, 400:{'description':'Bad Request'}, 401:{'desription':'Unauthorized'}}
)

