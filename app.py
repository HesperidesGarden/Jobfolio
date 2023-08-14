import os
from werkzeug.utils import secure_filename
from flask import Flask, session, render_template, redirect, url_for, request
from route_methods.project_form import project_form
from route_methods.portfolio import portfolio
from route_methods.account import account
from route_methods.signup import signup_user
from route_methods.portfolio_edit import portfolio_edit_view
from route_methods.update_profile import *
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


# SubmitProject Route
@app.route("/submit", methods=["POST"])
def submit_project():
    return redirect("/portfolio/")

# addSkill Route
@app.route('/edit_skill/', methods=["GET", "POST"])
def get_add_skill():
    return add_skill()


# addLang Route
@app.route('/edit_lang/', methods=["GET", "POST"])
def get_add_lang():
    return add_lang()

# deleteLang
@app.route('/delete_language/<int:language_id>', methods=['POST'])
def get_delete_language(language_id):
    return delete_language()

# deleteSkill
@app.route('/delete_skill/<int:skill_id>', methods=['POST'])
def get_delete_skill(skill_id):
    return delete_skill()


# UpdateProfile Route
@app.route('/update_user_profile', methods=['POST'])
def get_update_user_profile():
    return update_user_profile()





    
if __name__ == "__main__":
    # with app.app_context():
        # create_tables() 
    app.run(debug=True)
