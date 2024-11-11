from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,index=True,unique=True)
    email = Column(String,index=True,unique=True)
    hashed_password = Column(String)
    todos = relationship("Todo",back_populates="user")


