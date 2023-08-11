from flask import Flask, session, render_template, redirect, url_for, request
from dao.userDAO import UserDAO

def account():
    user_dao = UserDAO()
    
    if 'user_id' in session:
        user_id = session['user_id']
        user_data = user_dao.get_user_data(user_id)
        
        if user_data:
            return render_template('account.html', user=user_data)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    


