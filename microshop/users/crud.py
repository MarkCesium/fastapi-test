"""
---C.R.U.D.---
-Create
-Read
-Update
-Delete
"""
from microshop.users.schemas import CreateUser, GetUser

users: list[GetUser] = []


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    users.append(user)
    return {"success": True, "user": user}


def get_users() -> list[GetUser]:
    return users
