from pydantic import BaseModel
from enum import Enum

class Role(Enum):
    USER = 1
    ADMIN = 2

class UserBase(BaseModel):
    username: str
    email: str


# sign up
class SignUpUserRequest(UserBase):
    password: str
    pass

class SignUpUserResponse(UserBase):
    user_id: int
    active: bool
    role: Role

    class Config:
        orm_mode = True


# log in
class LoginUserRequest(BaseModel):
    username: str
    password: str

class LoginUserResponse(BaseModel):
    token: str
    token_type: str

    class Config:
        orm_mode = True

# refresh token
class RefreshUserTokenRequest(BaseModel):
    token: str

# current  user
class UserResponse(UserBase):
    user_id: int
    username: str
    email: str
    active: bool
    role: Role

    class Config:
        orm_mode = True

# forgot password
class ForgotPasswordRequest(BaseModel):
    email: str

#password
class ResetPasswordRequest(BaseModel):
    password: str

# update user
class UpdateProfileRequest(BaseModel):
    user_id: int | None = None
    username: str | None = None
    role: Role | None = None



    # sa.Column('id', sa.Integer, primary_key=True),
    # sa.Column('username', sa.String(255), nullable=False),
    # sa.Column('email', sa.String(255), nullable=False),
    # sa.Column('password', sa.String(255), nullable=False),
    # sa.Column('active', sa.Boolean, nullable=False),
    # sa.Column('role', sa.String(255), nullable=False, default='user'),