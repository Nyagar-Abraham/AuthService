from typing import Annotated, List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session

from service import user_crud_service

from dependencies import get_current_user_active_user, get_session
from models import UserPublic, User, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user_active_user)],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        201: {"description": "Created", "content": {"application/json": {}}},
        404: {"description": "Not found"}},
)

@router.get("" , response_model=List[UserPublic])
async def get_users(current_user: Annotated[User , Depends(get_current_user_active_user)], session: Session = Depends(get_session) ):
    users = user_crud_service.get_users(session)
    print(users)
    return users

@router.get("/me", response_model=UserPublic)
async def get_current_user(current_user: Annotated[User, Depends(get_current_user_active_user)]):
    return UserPublic.model_validate(current_user)

# @router.put("/update-profile/{user_id}", response_model=UserPublic)
# async def update_profile(user_id:int ,new_profile: UserUpdate , session:Session = Depends(get_session)):
#     user = update_user(db, user_id, new_profile)

