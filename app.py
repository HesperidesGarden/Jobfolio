import os
from werkzeug.utils import secure_filename
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.UsersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.LanguageDAO import LanguageDAO
from dao.ProjectDAO import ProjectDAO
from dao.SkillDAO import SkillDAO
from dao.userProfileDAO import UserProfileDAO
from route_methods.project_form import project_form
from route_methods.portfolio import portfolio
from route_methods.account import account
from route_methods.signup import signup_user

app = Flask(__name__)

app.config.from_mapping(
	SECRET_KEY='secret_key_just_for_dev_environment',
	DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

users_dao = UsersDAO()
education_dao = EducationDAO()
language_dao = LanguageDAO()
project_dao = ProjectDAO()
skill_dao = SkillDAO()
userProfile_DAO = UserProfileDAO()

UPLOAD_FOLDER = 'userpictures'  # Ordner für hochgeladene Bilder
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # Erlaubte Dateitypen

# Home = Default
@app.route('/')
def index():
	return redirect(url_for('get_home'))


# Login Route # chatgpt-generated
@app.route('/login/', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_dao.check_user_credentials(email, password)

        if user:
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
        user_first_name = UsersDAO.get_user_first_name(user_id)
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

# MyPortfolio Route
@app.route('/portfolio_edit/')
def get_portfolio_edit():
	return render_template('portfolio_edit_view.html') 

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

        SkillDAO.create_skill(user_id, skill_name, skill_proficiency, skill_description)

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

        LanguageDAO.create_language(user_id, language_name, language_proficiency, language_description)

        return redirect(url_for('get_portfolio'))  

    return render_template('portfolio_edit_view.html')  

# deleteLang
@app.route('/delete_language/<int:language_id>', methods=['DELETE'])
def delete_language(language_id):

    if LanguageDAO.delete_language(language_id):
        return redirect(url_for('get_portfolio'))  
    else:
         error_message = 'Error deleting.'
    return render_template('portfolio_edit_view.html', error_message=error_message)

# deleteSkill
@app.route('/delete_skill/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):

    if SkillDAO.deleteSkill(skill_id):
        return redirect(url_for('get_portfolio'))  
    else:
         error_message = 'Error deleting.'
    return render_template('portfolio_edit_view.html', error_message=error_message)

# SubmitProject Route
@app.route("/submit", methods=["POST"])
def submit_project():
    return redirect("/portfolio/")

# CreateProfile Route
@app.route('/create_profile', methods=['POST'])
def create_user_profile_picture():
    picture = request.files['profile_picture']
    user_id = session['user_id']

    users_dao.create_user_profile(picture, user_id)
    return redirect(url_for('get_home'))


# UpdateProfile Route
@app.route('/update_user_profile', methods=['POST'])
def update_user_profile():
    
    user_id = session['user_id']
    user_profile = userProfile_DAO.get_user_profile_by_user_id(user_id)

    if 'profile_picture' in request.files:
        profile_picture = request.files['profile_picture']

        if profile_picture and profile_picture.filename != '' and allowed_file(profile_picture.filename):
            filename = secure_filename(profile_picture.filename)
            picture_path = os.path.join('userpictures', filename)
            profile_picture.save(picture_path)

            title = request.form.get('user_name')  
            user_description = request.form.get('user_description')  

            if user_profile:
                userProfile_DAO.update_profile(user_id, picture_path, title, user_description)
            else:
                userProfile_DAO.create_user_profile(profile_picture, title, user_description, user_id)

            return redirect(url_for('get_portfolio')) 

    return "Error updating profile"



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

