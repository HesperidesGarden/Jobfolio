from flask import Flask, render_template, redirect, request, flash
from models import User
from db import db
import bcrypt


def signup_user():
    if request.method == "POST":
        
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        street = request.form["street"]
        zipcode = request.form["zipcode"]
        city = request.form["city"]
        password = request.form["password"]
        password_confirm = request.form["confirm_password"]
        
        # execute password checks - chatgpt generated 
        if password_confirm == password:
            if len(password) < 8:
                error_message = 'Password Insufficient'
                return render_template("signup.html", error_message=error_message)

            if not any(char.isdigit() for char in password):
                error_message = 'Password Insufficient'
                return render_template("signup.html", error_message=error_message)

            if not any(char.isalpha() for char in password):
                error_message = 'Password Insufficient'
                return render_template("signup.html", error_message=error_message)
        else:
            error_message = 'Passwords do not match.'
            return render_template("signup.html", error_message=error_message)

        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street=street,
            zipcode=zipcode,
            city=city,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/portfolio/")

    return render_template("signup.html")





