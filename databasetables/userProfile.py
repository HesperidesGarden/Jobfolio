from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    picture = Column(String)
    title = Column(String)
    short_description = Column(String)
    user_id = Column(Integer, ForeignKey('User.id'))

    user = relationship("User", back_populates="profile")
