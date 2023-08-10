from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from app.api.schemas.entity import Entity


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None
    contact_email: str
    contact_phone: Optional[str] = None
    publications_count: Optional[int] = 0


class AuthorCreate(AuthorBase):
    entity_id: Optional[int] = None
    twitter_link: Optional[str] = None
    facebook_link: Optional[str] = None
    linkedin_link: Optional[str] = None


class Author(AuthorCreate):
    id: int
    entity: Optional[Entity] = None
    created_at: datetime
    last_login: datetime

    class Config:
        orm_mode = True
