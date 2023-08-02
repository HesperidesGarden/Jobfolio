# chatgpt generated

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    description = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))

    # Beziehung zur User-Klasse herstellen
    user = relationship("users", back_populates="skills")

    def __repr__(self):
        return f"<Skill(id={self.id}, name={self.name}, proficiency={self.proficiency})>"
