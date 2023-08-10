from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EntityBase(BaseModel):
    name: str
    contact_email: str
    description: Optional[str] = None


class EntityCreate(EntityBase):
    website: Optional[str] = None
    contact_phone: Optional[str] = None


class Entity(EntityCreate):
    id: int
    created_at: datetime
