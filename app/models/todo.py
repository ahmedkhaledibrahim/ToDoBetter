from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class ToDo(Base):
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String)
    priority = Column(String)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User",back_populates="todos")