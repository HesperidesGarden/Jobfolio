from flask import Flask, render_template, redirect, request
from models import User
from db import db

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

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street=street,
            zipcode=zipcode,
            city=city,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/portfolio/")

    return render_template("signup.html")





