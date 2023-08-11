# chatgpt generated


from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field_of_study = Column(String)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    description = Column(String)
    users_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Education(id={self.id}, institution={self.institution}, degree={self.degree}, start_date={self.start_date}, end_date={self.end_date})>"
