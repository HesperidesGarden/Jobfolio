import os
from werkzeug.utils import secure_filename
from flask import Flask, session, render_template, redirect, url_for, request
from route_methods.project_form import project_form
from route_methods.portfolio import portfolio
from route_methods.account import account
from route_methods.signup import signup_user
from route_methods.portfolio_edit import portfolio_edit_view
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from db import db, create_tables
from models import *
import bcrypt



app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse',
    SQLALCHEMY_DATABASE_URI= 'sqlite:///jobfolio.sqlite'
)

db.init_app(app)
create_tables(app)
# from db import db, User, Education, Language, Project, Skill, UserProfile, create_tables

bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'userpictures'  # Ordner für hochgeladene Bilder
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # Erlaubte Dateitypen

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Home = Default
@app.route('/')
def index():
	return redirect(url_for('get_home'))


# Login Route # chatgpt-generated
@app.route('/login/', methods=['GET', 'POST'])
def get_login():
    error_message = 'Invalid login credentials'

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db.session.query(User).filter_by(email=email).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['user_id'] = user.id
            return redirect(url_for('get_portfolio')) 
        else:
            error_message = 'Invalid login credentials'
    return render_template('login.html', error_message=error_message)

# Home Route
@app.route('/home/')
def get_home():
    user_logged_in = 'user_id' in session
    user_first_name = None
    if user_logged_in:
        user_id = session['user_id']
        user_first_name = db.session.get(User, user_id).first_name
    return render_template('home.html', user_logged_in=user_logged_in, user_first_name=user_first_name)


# Account Route
@app.route('/account')
def get_account():
    return account()
    
# Logout Route
@app.route('/logout', methods=['POST'])
def get_logout():
    session.pop('user_id', None)
    return redirect(url_for('get_home'))

# FindJobs Route
@app.route('/findjobs/')
def get_findjobs():
	return render_template('findjobs.html') 

# MyPortfolio Route
@app.route('/portfolio/')
def get_portfolio():
    return portfolio()

# PortfolioEdit Route
@app.route('/portfolio_edit/')
def get_portfolio_edit():
	return portfolio_edit_view()

# ProjectForms Route
@app.route('/create_project/', methods=["GET", "POST"])
def get_project_form():
    return project_form()
   
# Signup Route
@app.route('/signup/', methods=["GET", "POST"])
def get_signup():
	return signup_user() 



# addSkill Route
@app.route('/edit_skill/', methods=["GET", "POST"])
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
@app.route('/edit_lang/', methods=["GET", "POST"])
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
@app.route('/delete_language/<int:language_id>', methods=['POST'])
def delete_language(language_id):
    language = db.session.get(Language, language_id)
    
    if language:
        db.session.delete(language)
        db.session.commit()
    else:
        error_message = 'Error deleting.'
    return redirect(url_for('get_portfolio'))

# deleteSkill
@app.route('/delete_skill/<int:skill_id>', methods=['POST'])
def delete_skill(skill_id):
    skill = db.session.get(Skill, skill_id)

    if skill:
        db.session.delete(skill)
        db.session.commit()
    else:
        error_message = 'Error deleting.'
    return redirect(url_for('get_portfolio'))

# SubmitProject Route
@app.route("/submit", methods=["POST"])
def submit_project():
    return redirect("/portfolio/")

# UpdateProfile Route
@app.route('/update_user_profile', methods=['POST'])
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

    return redirect(url_for('get_portfolio')) 




    
if __name__ == "__main__":
    # with app.app_context():
        # create_tables() 
    app.run(debug=True)
