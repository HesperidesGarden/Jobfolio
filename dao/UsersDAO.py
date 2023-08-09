
# chatgpt generated

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.users import User 
import bcrypt


# Verbindung zur SQLite-Datenbank herstellen
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

class UsersDAO:

    @classmethod
    def check_user_credentials(cls, email, password):
        user = session.query(User).filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user 
        else:
            return None



    @classmethod
    def create_user(cls, first_name, last_name, email, phone_number, street, zipcode, city, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street=street,
            zipcode=zipcode,
            city=city,
            password=hashed_password.decode('utf-8')
        )
        session.add(new_user)
        session.commit()
        return new_user
    
    @classmethod
    def get_user_first_name(cls, user_id):
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            return user.first_name
        else:
            return None
