import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import User, Education, Language, Project, Skill, UserProfile 
from db import db


def portfolio():
    if 'user_id' in session:
        user_id = session['user_id']

        user = db.session.get(User, user_id)
        user_profile = db.session.get(UserProfile, user_id)
        user_skills = db.session.query(Skill).filter_by(user_id=user_id).all()
        user_languages = db.session.query(Language).filter_by(user_id=user_id).all()


        return render_template('portfolio_logged_in.html',
                                user_profile_picture=user_profile.picture,
                                user_name=user.first_name+user.last_name,
                                user_occupation=user_profile.title,
                                user_description=user_profile.short_description,
                                user_skills=user_skills,
                                user_languages=user_languages
                                )

    return render_template('portfolio_logged_out.html')

