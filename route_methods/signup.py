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
        
        # execute password checks - chatgpt generated 
        if len(password) < 8:
            flash("Das Passwort muss mindestens 8 Zeichen lang sein.", "error")
            return render_template("signup.html")

        if not any(char.isdigit() for char in password):
            flash("Das Passwort muss mindestens eine Zahl enthalten.", "error")
            return render_template("signup.html")

        if not any(char.isalpha() for char in password):
            flash("Das Passwort muss mindestens einen Buchstaben enthalten.", "error")
            return render_template("signup.html")
        
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





