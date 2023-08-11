from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone_number = Column(String)
    street = Column(String)
    zipcode = Column(String)
    city = Column(String)
    password = Column(String)
    
<<<<<<< Updated upstream:databasetables/user.py
  #  userprofiles = relationship("UserProfile", back_populates="user")
    
=======
    user_profile = relationship("UserProfile", back_populates="user") 

>>>>>>> Stashed changes:model/user.py
    def __repr__(self):
        return f"<User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"
