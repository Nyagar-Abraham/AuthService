from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session

# from service.user_crud_service import update_user

from dependencies import get_current_user_active_user, get_session
from models import UserPublic, User, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_user_active_user)],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        201: {"description": "Created", "content": {"application/json": {}}},
        404: {"description": "Not found"}, },
)

@router.get("/me", response_model=UserPublic)
async def get_current_user(current_user: Annotated[User, Depends(get_current_user_active_user)]):
    return UserPublic.model_validate(current_user)

# @router.put("/update-profile/{user_id}", response_model=UserPublic)
# async def update_profile(user_id:int ,new_profile: UserUpdate , session:Session = Depends(get_session)):
#     user = update_user(db, user_id, new_profile)

