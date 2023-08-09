from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from app.api.schemas.user import User


class EntityBase(BaseModel):
    name: str
    description: Optional[str] = None
    creator_id: int


class EntityCreate(EntityBase):
    pass


class Entity(EntityBase):
    id: int
    created_at: datetime
    owner: User

    class Config:
        from_attributes = True
