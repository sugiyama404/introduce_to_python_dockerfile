from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    Password = Column(String(100), nullable=False)
    CreatedAt = Column(DateTime, default=datetime.now)
    UpdatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
