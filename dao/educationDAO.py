# chatgpt generated

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.education import Education

# Verbindung zur SQLite-Datenbank herstellen
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

class EducationDAO:
    @classmethod
    def get_education_by_user_id(cls, user_id):
        return session.query(Education).filter_by(users_id=user_id).all()

    @classmethod
    def create_education(user_id, institution, degree, field_of_study, start_date, end_date, description):
        new_education = Education(
            users_id=user_id,
            institution=institution,
            degree=degree,
            field_of_study=field_of_study,
            start_date=start_date,
            end_date=end_date,
            description=description
        )
        session.add(new_education)
        session.commit()
        return new_education

    # Weitere Methoden für Aktualisierung, Löschung usw.
