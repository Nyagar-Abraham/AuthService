from datetime import timezone, timedelta
from typing import Annotated

import jwt
from fastapi import HTTPException
from fastapi.params import Header, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from datetime import datetime

from jwt import InvalidTokenError
from pydantic import ValidationError
from sqlmodel import Session
from starlette import status

from config import settings
from database import engine
from models import User, TokenData

security = HTTPBearer()

def get_session():
    with Session(engine) as session:
        yield session


def get_user(user_id: int,  session: Session) -> User | None:
    db_user = session.get(User, user_id)
    if db_user is None:
        return None
    return User.model_validate(db_user)


async def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)], session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        email = payload.get("email")
        token_data = TokenData(user_id=user_id, email=email)
    except (InvalidTokenError, ValidationError) as e:
        print("JWT Decode Error:", str(e))
        raise credentials_exception
    user: User | None = get_user(user_id=int(token_data.user_id),session=session)
    if user is None:
        raise credentials_exception
    return user

async def get_current_user_active_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    if not current_user.active:
        raise HTTPException(status_code=400, detail="User is not active")
    return current_user


def create_access_token(data:dict):
    access_token_expire_delta = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    return create_token(data,access_token_expire_delta )

def create_refresh_token(data: dict):
    refresh_token_expire_delta = settings.REFRESH_TOKEN_EXPIRE_MINUTES
    return create_token(data, refresh_token_expire_delta )

def create_token(data:dict, expire_mins:int):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=expire_mins)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
