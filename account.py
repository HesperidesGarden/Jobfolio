from flask import Flask, session, render_template, redirect, url_for, request
from dao.usersDAO import UsersDAO

# momentan kommt man auf ne placeholder account seite
# placeholder daten mit db daten ersetzen, bräuchte dafür ein get_user_data oder so

# später die if/else bedingung (auskommetiert unten) wieder rausnehmen damit man als uneingeloggter auf login weitergeleitet wird

def account():
   # if 'user_id' in session:
    # Fetch user data from the database based on the session user_id
    # user = users_dao.get_user_by_id(session['user_id'])
        user = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone_number': '123-456-7890',
            'street': 'Street2',
            'zip_code': '12345',
            'city': 'Town'
        }
        return render_template('account.html', user=user)    
   # else:
   #     return render_template('login.html')
    


