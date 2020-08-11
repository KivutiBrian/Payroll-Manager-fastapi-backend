from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import timedelta, datetime

# model import
from models.user_model import User
# userservice import
from services.user_service import UserService
# schema
from schemas.user_schema import UserCreate,UserOut
# settings
from settings.db_setup import get_db, SessionLocal


router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str



# JWT CONFIGURATIONS
SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# create an obj to manage hashes and related configurations
pwd_context = CryptContext(schemes=['bcrypt'])

# define the url the client will use to access the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# authenticate user
def authenticate_user(username:str, password:str, db:Session = Depends(get_db)):

    user = db.query(User).filter(User.username==username).first()
    if not user:
        return False
    if not verify_password(plain_password=password, hashed_password=user.password):
        return False

    return user

# create access token
def create_access_token(data: dict,expires_delta:Optional[timedelta]=None ):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    
    # ENCODE TOKEN
    new_data =data.copy()
    new_data.update({'exp':expire})
    token = jwt.encode(claims=new_data, key=SECRET_KEY, algorithm=ALGORITHM)

    return token

# get user
def get_user(user_id:int):
    db:Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    return user

# create get user dependency
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception  
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f'{e}')

    user = get_user(user_id=user_id)
    
    if user is None:
        raise credentials_exception
    return user

#  get active user 
async def get_current_active_user(current_user: UserOut =  Depends(get_current_user)):
    if not current_user.active:
        raise HTTPException(status_code=400, detail='User account is deactivated')
    return current_user
    

@router.post('/register',
summary='create a new access token',
status_code=201,
response_model=UserOut
)
async def register(user:UserCreate, db:Session = Depends(get_db)):
    return UserService.create_user(payload=user, db=db)


@router.post('/token',
summary='login to get access token',
response_model=Token,
status_code=200
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = authenticate_user(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserOut)
async def read_users_me(current_user: UserOut = Depends(get_current_active_user)):
    return current_user
 
