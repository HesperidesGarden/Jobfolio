# chatgpt generated

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone_number = Column(String)
    street = Column(String)
    zipcode = Column(String)
    city = Column(String)
    password = Column(String)
    
    
def __repr__(self):
    return f"<User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"
