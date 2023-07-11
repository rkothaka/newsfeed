from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class FeedBase(BaseModel):
    content: str


class PostCreate(FeedBase):
    creator_id: Optional[int]
    entity_id: Optional[int]


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True