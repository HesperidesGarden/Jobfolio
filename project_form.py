from flask import Flask, render_template, redirect, request
from db import Project

def project_form():
    if request.method == "POST":
        project_name = request.form["project_name"]
        description = request.form["description"]
        role = request.form["role"]
        url_project = request.form["url_project"]
        picture = request.form["picture"]
        duration = request.form["duration"]
        difficulty = request.form["difficulty"]

        new_project = Project(
            title=project_name,
            description=description,
            role=role,
            url_project=url_project,
            url_picture=picture,
            duration=duration,
            difficulty=difficulty,
            user_id=session['user_id']
        )

        db.session.add(new_project)
        db.session.commit()
        return redirect("/portfolio/")

    return render_template("project_form.html")





