from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    phone_number = db.Column(db.String)
    street = db.Column(db.String)
    zipcode = db.Column(db.String)
    city = db.Column(db.String)
    password = db.Column(db.String)
    
    educations = db.relationship("Education", back_populates="user")
    languages = db.relationship("Language", back_populates="user")
    projects = db.relationship("Project", back_populates="user")
    skills = db.relationship("Skill", back_populates="user")
    user_profile = db.relationship("UserProfile", back_populates="user")


class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String, nullable=False)
    degree = db.Column(db.String, nullable=False)
    field_of_study = db.Column(db.String)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="educations")

class Language(db.Model):
    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String, nullable=False)
    proficiency = db.Column(db.String, nullable=False)
    self_evaluation = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="languages")

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    url_project = db.Column(db.String)
    url_picture = db.Column(db.String)
    duration = db.Column(db.String)
    difficulty = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="projects")

class Skill(db.Model):
    __tablename__ = 'skill'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    proficiency = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="skills")


class UserProfile(db.Model):
    __tablename__ = 'user_profile'

    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String)
    title = db.Column(db.String)
    short_description = db.Column(db.String(length=500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="user_profile", foreign_keys=[user_id])



def create_tables():
    with db.app.app_context():
        db.create_all()