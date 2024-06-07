from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
import pytz

import settings

Base = declarative_base()

tz = pytz.timezone(settings.time_zone)

class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String(100), nullable=True)
    Email = Column(String(100), nullable=True)
    Password = Column(String(100), nullable=True)
    CreatedAt = Column(DateTime, default=datetime.now(tz))
    UpdatedAt = Column(DateTime, default=datetime.now(tz), onupdate=datetime.now(tz))
