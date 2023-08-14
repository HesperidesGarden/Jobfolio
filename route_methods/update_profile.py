import os
from werkzeug.utils import secure_filename
from flask import Flask, session, render_template, redirect, url_for, request
from db import db, create_tables
from models import *

UPLOAD_FOLDER = 'userpictures'  # Ordner für hochgeladene Bilder
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # Erlaubte Dateitypen

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# addSkill Route
def add_skill():
    user_id = session['user_id']
    
    if request.method == 'POST':
        skill_name = request.form['skill_name']
        skill_proficiency = request.form['skill_proficiency']
        skill_description = request.form['skill_description']

        new_skill = Skill(name=skill_name, proficiency=skill_proficiency, description=skill_description, user_id=user_id)
        db.session.add(new_skill)
        db.session.commit()

        return redirect(url_for('get_portfolio')) 

    return render_template('portfolio_edit_view.html') 


# addLang Route
def add_lang():
    user_id = session['user_id']
    if request.method == 'POST':
        language_name = request.form['language_name']
        language_proficiency = request.form['language_proficiency']
        language_description = request.form['language_description']

        new_language = Language(language_name=language_name, proficiency=language_proficiency, self_evaluation=language_description, user_id=user_id)
        db.session.add(new_language)
        db.session.commit()

        return redirect(url_for('get_portfolio'))  

    return render_template('portfolio_edit_view.html')  

# deleteLang
def delete_language(language_id):
    language = db.session.get(Language, language_id)
    
    if language:
        db.session.delete(language)
        db.session.commit()
    else:
        error_message = 'Error deleting.'
    return redirect(url_for('get_portfolio'))

# deleteSkill
def delete_skill(skill_id):
    skill = db.session.get(Skill, skill_id)

    if skill:
        db.session.delete(skill)
        db.session.commit()
    else:
        error_message = 'Error deleting.'
    return redirect(url_for('get_portfolio'))


# UpdateProfile Route
def update_user_profile():
    user_id = session['user_id']
    user_profile = UserProfile.query.filter_by(user_id=user_id).first()

    profile_picture = request.files['profile_picture']
    title = request.form.get('user_occupation')  
    user_description = request.form.get('user_description') 
    
    picture_path = None
    if profile_picture and profile_picture.filename != '' and allowed_file(profile_picture.filename):
        picture_path = os.path.join('userpictures', profile_picture.filename)
        profile_picture.save(picture_path)

    if user_profile:
        user_profile.title = title
        user_profile.short_description = user_description
        if picture_path:
            user_profile.picture = picture_path
    else:
        new_user_profile = UserProfile(picture=picture_path, title=title, short_description=user_description, user_id=user_id)
        db.session.add(new_user_profile)

    db.session.commit()




