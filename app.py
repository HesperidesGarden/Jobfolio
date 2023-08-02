import os
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.usersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.languageDAO import LanguageDAO
from dao.projectDAO import ProjectDAO
from dao.skillDAO import SkillDAO




app = Flask(__name__)

app.config.from_mapping(
	SECRET_KEY='secret_key_just_for_dev_environment',
	DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

users_dao = UsersDAO()
education_dao = EducationDAO
language_dao = LanguageDAO
project_dao = ProjectDAO
skill_dao = SkillDAO


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
@app.route('/myportfolio/')
def myportfolio():
	return render_template('myportfolio.html') 





@app.route('/lists/')
def get_lists():
	sql_query = 'SELECT * from list ORDER BY name'
	db_con = db.get_db_con()
	lists_temp = db_con.execute(sql_query).fetchall()
	lists = []
	for list_temp in lists_temp:
		list = dict(list_temp)
		sql_query = (
			'SELECT COUNT(complete) = SUM(complete) '
			'AS complete FROM todo '
			f'JOIN todo_list ON list_id={list["id"]} '
				'AND todo_id=todo.id; '
		)
		complete = db_con.execute(sql_query).fetchone()['complete']
		list['complete'] = complete
		lists.append(list)
	if request.args.get('json') is not None:
		return lists
	else:
		return render_template('lists.html', lists=lists)

@app.route('/lists/<int:list_id>')
def get_list_todos(list_id):
	sql_query_1 = f'SELECT name FROM list WHERE id={list_id}'
	sql_query_2 = (
		'SELECT id, complete, description FROM todo '
		f'JOIN todo_list ON todo_id=todo.id AND list_id={list_id} '
		'ORDER BY id;'
	)
	db_con = db.get_db_con()
	list = {}
	list['name'] = db_con.execute(sql_query_1).fetchone()['name']
	list['todos'] = db_con.execute(sql_query_2).fetchall()
	if request.args.get('json') is not None:
		list['todos'] = [dict(todo) for todo in list['todos']]
		return list
	else:
		return render_template('todos.html', list=list)

@app.route('/insert/sample')
def run_insert_sample():
	db.insert_sample()
	return 'Database flushed and populated with some sample data.'

