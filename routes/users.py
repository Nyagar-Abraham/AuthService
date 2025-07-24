from fastapi import APIRouter
from fastapi.params import Depends

from schema import LoginUserResponse, UserResponse, UpdateProfileRequest

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends()],
    responses={
        200: {"description": "Success", "content": {"application/json": {}}},
        201: {"description": "Created", "content": {"application/json": {}}},
        404: {"description": "Not found"}, },
)

@router.get("/me", response_model=LoginUserResponse)
async def get_current_user():
    pass

@router.put("/update-profile", response_model=UserResponse)
async def update_profile(new_profile: UpdateProfileRequest ):
    pass
