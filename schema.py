# from datetime import datetime
#
# from pydantic import BaseModel, EmailStr, ConfigDict
# from enum import Enum
#
# class Role(Enum):
#     USER = "user"
#     ADMIN = "admin"
#
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#
#
# # sign up
# class SignUpUserRequest(UserBase):
#     password: str
#
#
# class SignUpUserResponse(UserBase):
#     model_config = ConfigDict(from_attributes=True)
#
#     id: int
#     active: bool
#     role: Role
#     created_at: datetime
#
# # log in
# class LoginUserRequest(BaseModel):
#     email: str
#     password: str
#
# class Token(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#
#     token: str
#     token_type: str
#
# class TokenData(BaseModel):
#     user_id: str
#     email: str
#
# # refresh token
# class RefreshUserTokenRequest(BaseModel):
#     token: str
#
# # current  user
# class UserResponse(UserBase):
#     model_config = ConfigDict(from_attributes=True)
#
#     id: int
#     username: str
#     email: str
#     active: bool
#     role: Role
#     created_at: datetime
#
#
#
# # forgot password
# class ForgotPasswordRequest(BaseModel):
#     email: str
#
# #password
# class ResetPasswordRequest(BaseModel):
#     password: str
#
# # update user
# class UpdateProfileRequest(BaseModel):
#     username: str | None = None
#     role: Role | None = None
#     active: bool
#
#
# class UserInDB(UserBase):
#     model_config = ConfigDict(from_attributes=True)
#
#     id: int
#     password: str
#     active: bool
#     role: Role
#     created_at: datetime
#
#
#
#
#     # sa.Column('id', sa.Integer, primary_key=True),
#     # sa.Column('username', sa.String(255), nullable=False),
#     # sa.Column('email', sa.String(255), nullable=False),
#     # sa.Column('password', sa.String(255), nullable=False),
#     # sa.Column('active', sa.Boolean, nullable=False),
#     # sa.Column('role', sa.String(255), nullable=False, default='user'),