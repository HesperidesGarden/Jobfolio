from flask import Flask, render_template, redirect, request
from dao.userDAO import UserDAO

def signup_user():
    user_dao = UserDAO()

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        street = request.form["street"]
        zipcode = request.form["zipcode"]
        city = request.form["city"]
        password = request.form["password"]

        user_dao.create_user(first_name, 
                             last_name, 
                             email, 
                             phone_number, 
                             street,
                             zipcode, 
                             city, 
                             password)

        return redirect("/portfolio/")

    return render_template("signup.html")





