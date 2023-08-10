from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.core.database import Base


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    website = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
