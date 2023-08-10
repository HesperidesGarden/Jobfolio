from flask import Flask, render_template, redirect, request
from dao.projectDAO import ProjectDAO

project_dao = ProjectDAO
def project_form():
    if request.method == "POST":
        project_name = request.form["project_name"]
        description = request.form["description"]
        role = request.form["role"]
        url_project = request.form["url_project"]
        picture = request.form["picture"]
        duration = request.form["duration"]
        difficulty = request.form["difficulty"]

        project_dao.create_project(project_name=project_name,
                       description=description,
                       role=role,
                       url_project=url_project,
                       picture=picture,
                       duration=duration,
                       difficulty=difficulty)

        return redirect("/portfolio/")

    return render_template("project_form.html")





