from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validate_arguments

from app.api.schemas.author import Author
from app.api.schemas.entity import Entity


class FeedBase(BaseModel):
    title: str
    body: str


class FeedCreate(FeedBase):
    author_id: Optional[int] = None
    entity_id: Optional[int] = None

    @classmethod
    @validate_arguments
    def check_at_least_one_field(cls, author_id, entity_id):
        if author_id is None and entity_id is None:
            raise ValueError("At least one of 'creator_id' or 'entity_id' must be provided")
        return author_id or entity_id


class Feed(FeedBase):
    id: int
    created_at: datetime
    author_id: Optional[int] = None
    author: Optional[Author] = None
    entity_id: Optional[int] = None
    entity: Optional[Entity] = None
    likes_count: int
    media_id: Optional[int] = None
    media: Optional[str] = None

    class Config:
        from_attributes = True
