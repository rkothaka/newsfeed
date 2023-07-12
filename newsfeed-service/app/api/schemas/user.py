from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None
    email: str


class UserCreate(UserBase):
    mobile: Optional[str] = None


class User(UserCreate):
    id: int
    created_at: datetime
    last_login: datetime

    class Config:
        from_attributes = True
