# chatgpt generated

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

user = relationship("User", back_populates="Skill")  


class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<Skill(id={self.id}, name={self.name}, proficiency={self.proficiency})>"
