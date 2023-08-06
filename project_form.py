from flask import Flask, render_template, redirect, request
from dao.ProjectDAO import create_project
from app import app


@app.route("/project_form/", methods=["GET", "POST"])
def project_form():
    if request.method == "POST":
        project_name = request.form["project_name"]
        description = request.form["description"]
        role = request.form["role"]
        url_project = request.form["url_project"]
        picture = request.form["picture"]
        duration = request.form["duration"]
        difficulty = request.form["difficulty"]

        create_project(project_name=project_name,
                       description=description,
                       role=role,
                       url_project=url_project,
                       picture=picture,
                       duration=duration,
                       difficulty=difficulty)

        # Führe die Umleitung zur Portfolio-Seite durch
        return redirect("/portfolio/")

    return render_template("project_form.html")

# Neue URL-Regel für den submit_project-Endpunkt hinzufügen
@app.route("/submit", methods=["POST"])
def submit_project():
    # Hier kann die Logik für das Hinzufügen des Projekts in die Datenbank erfolgen (falls nötig)
    return redirect("/portfolio/")



