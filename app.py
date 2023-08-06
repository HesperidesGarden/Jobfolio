import os
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.UsersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.LanguageDAO import LanguageDAO
from dao.ProjectDAO import ProjectDAO
from dao.SkillDAO import SkillDAO

# .\venv\Scripts\activate.bat


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
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_dao.login(email, password)

        if user:
            return redirect(url_for('home'))  # Weiterleitung zur '/home/'-Route in app.py
        else:
            return 'Ungültige Anmeldedaten'

    return render_template('login.html')


@app.route('/logout')
def logout():
    users_dao.logout()
    return redirect(url_for('/'))

# FindJobs Route
@app.route('/findjobs/')
def get_findjobs():
	return render_template('findjobs.html') 

# SkillMatch Route
@app.route('/skillmatch/')
def get_skillmatch():
	return render_template('skillmatch.html') 

# MyPortfolio Route
@app.route('/portfolio/')
def get_portfolio():
	return render_template('portfolio.html') 
