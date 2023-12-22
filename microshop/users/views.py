from typing import Annotated

from fastapi import APIRouter

from microshop.users.schemas import CreateUser, GetUser
from microshop.users import crud


router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users() -> list[GetUser]:
    return crud.get_users()


@router.post("/")
async def create_user(user: CreateUser) -> dict:
    result = crud.create_user(user_in=user)
    if result["success"]:
        return {"message": "success", "email": user.email, "username": user.username}
    else:
        return {"message": "error"}
