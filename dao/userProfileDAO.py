import os
from werkzeug.utils import secure_filename

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.userProfile import UserProfile
from flask import url_for

# connect to database
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# start session
Session = sessionmaker(bind=engine)
session = Session()

class UserProfileDAO:
    
    def create_user_profile(self, picture, title, short_description, user_id):
        if picture:
            filename = secure_filename(picture.filename)
            picture_path = os.path.join('userpictures', filename)
            picture.save(picture_path)
        else:
            picture_path = None

        new_profile = UserProfile(
            picture=picture_path,  # Use picture_path here
            title=title,
            short_description=short_description,
            user_id=user_id
        )
        session.add(new_profile)
        session.commit()
        return new_profile
    
    def update_profile(self, user_id, picture_path, title, short_description):
        user_profile = session.query(UserProfile).filter_by(user_id=user_id).first()
        if user_profile:
            if picture_path:
                user_profile.picture = picture_path
            user_profile.title = title
            user_profile.short_description = short_description
            session.commit() 
            return user_profile
        return None

    @classmethod
    def get_user_profile_by_user_id(cls, user_id):
        user_profile = session.query(UserProfile).filter_by(user_id=user_id).first()
        return user_profile

    
    # stuff for portfolio profile
        
    @classmethod
    def get_user_profile_picture(cls, user_id):
        user_profile = session.query(UserProfile).filter_by(user_id=user_id).first()
        if user_profile and user_profile.picture:
            return user_profile.picture
        else:
             return url_for('static', filename='default-pfp.jpg')

    @classmethod
    def get_user_occupation(cls, user_id):
        user_profile = session.query(UserProfile).filter_by(user_id=user_id).first()
        if user_profile and user_profile.title:
            return user_profile.title
        else:
            return "Title not specified"

    @classmethod
    def get_user_description(cls, user_id):
        user_profile = session.query(UserProfile).filter_by(user_id=user_id).first()
        if user_profile and user_profile.short_description:
            return user_profile.short_description
        else:
            return "Description not available"
