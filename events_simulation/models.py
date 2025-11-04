import urllib
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import TIMESTAMP
# from base import Base

Base = declarative_base()

class Events(Base):
    __tablename__ = 'events'  # Table name in the database
    event_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String(450), unique=False, nullable=True)
    timestamp = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<event(event_id={self.id}, user_name='{self.user_name}', timestamp='{self.timestamp}')>"
    
class Events_Clone(Base):
    __tablename__ = 'events_clone'  # Table name in the database
    event_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    timestamp = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<event_clone(event_id={self.id}, user_name='{self.user_name}', timestamp='{self.timestamp}')>"
