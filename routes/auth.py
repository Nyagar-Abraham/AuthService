
from typing import Annotated

from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.params import Depends
from sqlmodel import Session
from starlette.responses import Response

from dependencies import create_access_token,create_refresh_token, get_current_user_active_user
from producers.kafka_producer import produce_kafka_signup_message
from producers.produce_schema import SignupMessage

from service import auth_crud_service

from models import User, UserPublic, UserCreate, Token, UserLogin
from dependencies import get_session


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        201: {"description": "Created", "content": {"application/json": {}}},
        404: {"description": "Not found"},},
)

@router.post('/signup', response_model=UserPublic)
async def signup(signup_request: UserCreate,background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    user = auth_crud_service.signup(session, signup_request)
    if user is None:
        raise HTTPException(status_code=400, detail="Bad request")

    message = SignupMessage(
        id=user.id,
        username=user.username,
        email=user.email,
    )
    background_tasks.add_task(produce_kafka_signup_message, message)
    return user

@router.post('/login', response_model=Token)
async def login(user_payload : UserLogin, response: Response, session: Session = Depends(get_session)):
     user:User = auth_crud_service.authenticate_user(session, user_payload)
     if user is None:
         raise  HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
     access_token = create_access_token(
         data={"sub": str(user.id),"email": user.email},
     )
     refresh_token = create_refresh_token(
         data={"sub": str(user.id), "email": user.email},
     )

     response.set_cookie(key="refresh_token", value=refresh_token)

     return Token(
         access_token=access_token,
         token_type="bearer",
     )


@router.post("/refresh", response_model=Token)
async def refresh(current_user:Annotated[User, Depends(get_current_user_active_user)]):
    print(f"user: {current_user.id}")

    access_token = create_access_token(
        data={"sub": current_user.id , "email": current_user.email},
    )
    return Token(
        access_token=access_token,
        token_type="bearer",
    )

# @router.post("/forgot-password")
# async def forgot_password(current_user:Annotated[UserInDB, Depends(get_current_user_active_user)]):
#     print(f"user: {current_user.id}")
#     pass
#
# @router.post("/reset-password", response_model=Token)
# async def reset_password(current_user:Annotated[UserInDB, Depends(get_current_user_active_user)]):
#     print(f"user: {current_user.id}")
#     pass

