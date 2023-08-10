from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.userProfile import UserProfile

# connect to database
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# start session
Session = sessionmaker(bind=engine)
session = Session()

class UserProfileDAO:
    def __init__(self, session: Session):
        self.session = session

    def create_user_profile(self, picture, title, short_description, user_id):
        new_profile = UserProfile(
            picture=picture,
            title=title,
            short_description=short_description,
            user_id=user_id
        )
        self.session.add(new_profile)
        self.session.commit()
        return new_profile

    def get_user_profile(self, user_id):
        return self.session.query(UserProfile).filter_by(user_id=user_id).first()
