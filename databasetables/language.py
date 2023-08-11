# chatgpt generated


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    language_name = Column(String, nullable=False)
    proficiency = Column(String, nullable=False)
    self_evaluation = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    
    user = relationship("User", back_populates="Language")


    def __repr__(self):
        return f"<Language(id={self.id}, language_name={self.language_name}, proficiency={self.proficiency})>"
