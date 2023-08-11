from flask import Flask, session, render_template, redirect, url_for, request
from dao.usersDAO import UsersDAO

def account():
    if 'user_id' in session:
        user_id = session['user_id']
        user_data = UsersDAO.get_user_data(user_id)
        
        if user_data:
            return render_template('account.html', user=user_data)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    


