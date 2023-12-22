from typing import Annotated
from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4


class CreateUser(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: Annotated[str, MaxLen(24), MinLen(2)]
    # username: str = Field(..., min_length=2, max_length=24)
    email: EmailStr
    password: Annotated[str, MaxLen(50), MinLen(6)]


class GetUser(BaseModel):
    id: UUID
    username: Annotated[str, MaxLen(24), MinLen(2)]
    email: EmailStr
