from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, DefaultClause
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from core.database import Base


class Feed(Base):
    __tablename__ = "feeditems"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    creator_id = Column(Integer, ForeignKey("users.id", ondelete="SET DEFAULT",
                                            name="fk_feed_user"), server_default=DefaultClause("-9999999"))
    entity_id = Column(Integer, ForeignKey("users.id", ondelete="SET DEFAULT",
                                           name="fk_feed_entity"), server_default=DefaultClause("-9999999"))
    likes_count = Column(Integer, server_default="0")
    media_id = Column(Integer, ForeignKey("media.id", ondelete="SET NULL",
                                          name="fk_feed_media"), nullable=True)

    owner = relationship("User")
    entity = relationship("Entity")
    media = relationship("Media")
    
    __table_args__ = (
        CheckConstraint(
            "creator_id IS NOT NULL OR entity_id IS NOT NULL",
            name="at_least_one_not_null"
        ),
    )
