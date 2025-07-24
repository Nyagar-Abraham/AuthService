from http.client import responses

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from service import auth_crud_service

from schema import LoginUserResponse, LoginUserRequest, SignUpUserRequest, SignUpUserResponse, ForgotPasswordRequest

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends()],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        201: {"description": "Created", "content": {"application/json": {}}},
        404: {"description": "Not found"},},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/signup', response_model=SignUpUserResponse)
async def signup(signup_request: SignUpUserRequest, db: Session = Depends(get_db)):
    user = auth_crud_service.signup(db, signup_request)
    if user is None:
        raise HTTPException(status_code=400, detail="Bad request")
    return user

@router.post('/login', response_model=LoginUserResponse)
async def login(user: LoginUserRequest ):
    pass
@router.post("/refresh", response_model=LoginUserResponse)
async def refresh(user: LoginUserRequest):
    pass


@router.post("/forgot-password")
async def forgot_password(user: ForgotPasswordRequest):
    pass

@router.post("/reset-password", response_model=LoginUserResponse)
async def reset_password(user: LoginUserRequest):
    pass

