import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from databasetables.user import User

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    picture = Column(String)
    title = Column(String)
    short_description = Column(String(length=500))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    #user = relationship("User", back_populates="user_profile")  # Use "User" instead of "users"


def get_picture_path(self):
    return os.path.join('userpictures', self.picture) if self.picture else None
    
        
def __repr__(self):
    return f"<UserProfile(id={self.id}, title={self.title}, user_id={self.user_id})>"
