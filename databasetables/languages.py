# chatgpt generated


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    language_name = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    self_evaluation = Column(String)
    users_id = Column(Integer, ForeignKey('users.id'))

    # Beziehung zur User-Klasse herstellen
    user = relationship("users", back_populates="languages")

    def __repr__(self):
        return f"<Language(id={self.id}, language_name={self.language_name}, proficiency={self.proficiency})>"
