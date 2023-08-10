from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.core.database import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE",
                                           name="fk_feed_author"), nullable=True)
    entity_id = Column(Integer, ForeignKey("entities.id", ondelete="CASCADE",
                                           name="fk_feed_entity"), nullable=True)
    likes_count = Column(Integer, server_default="0")
    media_id = Column(Integer, ForeignKey("media.id", ondelete="SET NULL",
                                          name="fk_feed_media"), nullable=True)

    author = relationship("Author", foreign_keys=[author_id])
    entity = relationship("Entity", foreign_keys=[entity_id])
    media = relationship("Media", foreign_keys=[media_id])

    __table_args__ = (
        CheckConstraint(
            "author_id IS NOT NULL OR entity_id IS NOT NULL",
            name="at_least_one_not_null"
        ),
    )
