from flask import Flask, session, render_template, redirect, url_for, request
from db import db, User

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
    


