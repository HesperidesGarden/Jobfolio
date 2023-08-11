# chatgpt generated

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


user = relationship("User", back_populates="Project")

# Basis-Klasse für die Deklaration der Datenbanktabellen
Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    role = Column(String)
    url_project = Column(String)
    url_picture = Column(String)
    duration = Column(String)
    difficulty = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<Project(id={self.id}, title={self.title}, description={self.description})>"
