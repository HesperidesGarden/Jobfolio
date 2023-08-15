from flask import session, render_template
from sqlalchemy import create_engine
from models import User, Language, Project, Skill, UserProfile
from db import db


def portfolio_edit_view():
    if 'user_id' in session:
        user_id = session['user_id']

        user = db.session.get(User, user_id)
        user_profile = db.session.get(UserProfile, user_id)
        user_projects = db.session.query(Project).filter_by(user_id=user_id).all()
        user_skills = db.session.query(Skill).filter_by(user_id=user_id).all()
        user_languages = db.session.query(Language).filter_by(user_id=user_id).all()

    if user_profile:
        return render_template('portfolio_edit_view.html',
                                user_occupation=user_profile.title,
                                user_description=user_profile.short_description,
                                user_projects=user_projects,
                                user_skills=user_skills,
                                user_languages=user_languages
                                )

    else :  
        return render_template('portfolio_edit_view.html',
                                user_occupation=None,
                                user_description=None,
                                user_projects=user_projects,
                                user_skills=user_skills,
                                user_languages=user_languages
                                )



