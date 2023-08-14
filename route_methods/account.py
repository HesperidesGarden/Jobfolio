from flask import Flask, session, render_template, redirect, url_for, request
from models import User, Language, Project, Skill, UserProfile 
from db import db

def account():
    if 'user_id' in session:
        user_id = session['user_id']
        user = db.session.get(User, user_id)
        
        if user:
            return render_template('account.html', user=user)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    


