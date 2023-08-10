from sqlalchemy import Column, Integer, String, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.core.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    bio = Column(String)
    publications_count = Column(Integer, nullable=False, default=0)

    # Social
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String)
    twitter_link = Column(String)
    facebook_link = Column(String)
    linkedin_link = Column(String)

    entity_id = Column(Integer, ForeignKey("entities.id", name="fk_author_entity"), nullable=True)
    last_login = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

    entity = relationship("Entity")
