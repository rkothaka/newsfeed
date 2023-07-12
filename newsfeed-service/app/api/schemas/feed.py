from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validate_arguments


class FeedBase(BaseModel):
    content: str


class FeedCreate(FeedBase):
    creator_id: Optional[int] = None
    entity_id: Optional[int] = None

    @classmethod
    @validate_arguments
    def check_at_least_one_field(cls, creator_id, entity_id):
        if creator_id is None and entity_id is None:
            raise ValueError("At least one of 'creator_id' or 'entity_id' must be provided")
        return creator_id or entity_id


class Feed(FeedBase):
    id: int
    created_at: datetime
    creator_id: int
    creator: None
    entity_id: int
    entity: None
    likes_count: int
    media_id: int
    media: None

    class Config:
        from_attributes = True
