from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr = Field(..., examples=["fastapi@packt.com"])
    events: Optional[List[Event]] = Field(None, examples=[])


class NewUser(User):
    password: str = Field(..., examples=["strong!!!"])


class UserSignIn(BaseModel):
    email: EmailStr = Field(..., examples=["fastapi@packt.com"])
    password: str = Field(
        ...,
        examples=[
            "strong!!!",
        ],
    )
