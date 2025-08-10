
from typing import Optional

from enum import Enum
from sqlmodel import Boolean, Column, Integer, String, DateTime, SQLModel, Field

from datetime import datetime

class Role(Enum):
    USER = "user"
    ADMIN = "admin"

class UserBase(SQLModel):
    username: str
    email: str


class User(UserBase , table=True):
    __tablename__ = 'users'

    id : int = Field(default=None, primary_key=True)
    password : str
    active : bool = True
    role : str = Role.USER.value
    created_at : datetime = datetime.now()

class UserCreate(UserBase):
    password: str

class UserUpdate(SQLModel):
    username: Optional[str] = None
    active: Optional[bool] = None
    role: Optional[Role] = None

class UserPublic(UserBase):
    id: int
    active: bool
    created_at : datetime
    role: Role

class UserLogin(SQLModel):
    email: str
    password: str

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    user_id: str
    email: str


class Profile(SQLModel):
    __tablename__ = 'profiles'

    id: int
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    boi: Optional[str] = None
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

