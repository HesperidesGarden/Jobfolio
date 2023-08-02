from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.skill import Skill  

# Verbindung zur SQLite-Datenbank herstellen
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

class SkillsDAO:
    @classmethod
    def get_skills_by_user_id(cls, user_id):
        return session.query(Skill).filter_by(users_id=user_id).all()

    @classmethod
    def create_skill(cls, user_id, name, proficiency, description):
        new_skill = Skill(
            users_id=user_id,
            name=name,
            proficiency=proficiency,
            description=description
        )
        session.add(new_skill)
        session.commit()
        return new_skill

    # Weitere Methoden für Aktualisierung, Löschung usw.
