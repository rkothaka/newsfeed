from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    last_login = Column(TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now())
