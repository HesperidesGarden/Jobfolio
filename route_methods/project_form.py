from flask import Flask, render_template, redirect, request, session,url_for
from models import Project
from db import db

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

#deleteProject
def delete_project(project_id):
    project = db.session.get(Project, project_id)

    if project:
        db.session.delete(project)
        db.session.commit()
    else:
        error_message = 'Error deleting.'
    return redirect(url_for('get_portfolio'))
