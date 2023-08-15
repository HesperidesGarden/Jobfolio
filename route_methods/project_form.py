import os
from werkzeug.utils import secure_filename
from flask import Flask, session, render_template, redirect, url_for, request
from db import db, create_tables
from models import *
import posixpath

UPLOAD_FOLDER = 'static/project_pictures'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def project_form():
    if request.method == "POST":
        project_name = request.form["project_name"]
        description = request.form["description"]
        role = request.form["role"]
        url_project = request.form["url_project"]
        duration = request.form["duration"]
        difficulty = request.form["difficulty"]
        
        # Handle picture upload
        picture = request.files["picture"]
        if picture and allowed_file(picture.filename):
            picture_filename = secure_filename(picture.filename)
            picture_path = os.path.join(UPLOAD_FOLDER, picture_filename)
            picture.save(picture_path)
            picture_url = "/" + picture_path
        else:
            picture_url = None

        new_project = Project(
            title=project_name,
            description=description,
            role=role,
            url_project=url_project,
            url_picture=picture_url,
            duration=duration,
            difficulty=difficulty,
            user_id=session['user_id']
        )

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('get_portfolio'))

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