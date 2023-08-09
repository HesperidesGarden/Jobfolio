import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.UsersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.LanguageDAO import LanguageDAO
from dao.ProjectDAO import ProjectDAO
from dao.SkillDAO import SkillDAO
from project_form import project_form
from portfolio import portfolio
from account import account
from signup import signup_user

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
            return 'Invalid login credentials'
    return render_template('login.html')


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

@app.route("/submit", methods=["POST"])
def submit_project():
    return redirect("/portfolio/")





# TEST ROUTE FÜR HTML SHIT MUSS ENTFERNT WERDEN AM ENDE
# ---
# ---
# ---
@app.route('/test/')
def portfolio_logged_in():
	return render_template('portfolio_logged_in.html') 
