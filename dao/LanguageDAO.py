
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.language import Language 

# connect to database
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# start session
Session = sessionmaker(bind=engine)
session = Session()

class LanguageDAO:
    @classmethod
    def get_languages_by_user_id(cls, user_id):
        return session.query(Language).filter_by(users_id=user_id).all()

    @classmethod
    def create_language(cls, user_id, language_name, proficiency, self_evaluation):
        new_language = Language(
            users_id=user_id,
            language_name=language_name,
            proficiency=proficiency,
            self_evaluation=self_evaluation
        )
        session.add(new_language)
        session.commit()
        return new_language
    
    @classmethod
    def delete_language(cls, id):
        language = session.query(Language).get(id)
        if language:
            session.delete(language)
            session.commit()
            return True  
        else:
            return False

