import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.usersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.languageDAO import LanguageDAO
from dao.projectDAO import ProjectDAO
from dao.skillDAO import SkillDAO
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

# Home Route
@app.route('/home/')
def get_home():
	return render_template('home.html') 

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

# Account Route
@app.route('/account')
def get_account():
    return account()
    
# Logout Route
@app.route('/logout')
def get_logout():
    users_dao.logout()
    return redirect(url_for('/'))

# FindJobs Route
@app.route('/findjobs/')
def get_findjobs():
	return render_template('findjobs.html') 

# MyPortfolio Route
@app.route('/portfolio/')
def get_portfolio():
    return portfolio()

@app.route('/edit_portfolio/')
def get_edit_portfolio():
	return render_template('edit_portfolio.html') 

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
