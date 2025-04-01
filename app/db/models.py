from sqlalchemy import Column, Integer, String, Boolean

from app.db.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    # username = Column(String, unique=True, index=True, nullable=False)
    hashed_password=Column(String, nullable=False)
    full_name=Column(String),
    is_active=Column(Boolean, default=True)
    # is_premium = Column(Boolean, default=False)


















































