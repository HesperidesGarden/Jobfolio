from flask import session, render_template
from sqlalchemy import create_engine
from models import User, Language, Skill, UserProfile, Project
from db import db
from flask import session, render_template, request, jsonify
import json


def portfolio(json_response=False):
    if 'user_id' in session:
        user_id = session['user_id']

        user = db.session.get(User, user_id)
        user_profile = db.session.get(UserProfile, user_id)
        user_projects = db.session.query(Project).filter_by(user_id=user_id).all()
        user_skills = db.session.query(Skill).filter_by(user_id=user_id).all()
        user_languages = db.session.query(Language).filter_by(user_id=user_id).all()

        portfolio_data = {
            "user_profile_picture": user_profile.picture if user_profile else "/static/default-pfp.jpg",
            "user_name": user.first_name + " " + user.last_name,
            "user_occupation": user_profile.title if user_profile else "Occupation not set.",
            "user_description": user_profile.short_description if user_profile else "No user description provided.",
            "user_projects": [],
            "user_skills": [],
            "user_languages": []
        }

        # adding profile picture to folder chatgpt generated
        if user_projects and user_projects != "No projects added.":
            for project in user_projects:
                portfolio_data["user_projects"].append({
            "image_url": project.url_picture,
            "title": project.title,
            "description": project.description,
            "id": project.id  
        })

        else:
            portfolio_data["user_projects"] = "No projects added."


        if user_skills:
            for skill in user_skills:
                portfolio_data["user_skills"].append({
                    "name": skill.name,
                    "proficiency": skill.proficiency,
                    "description": skill.description
                })
        else:
            portfolio_data["user_skills"] = "No skills added."

        if user_languages:
            for language in user_languages:
                portfolio_data["user_languages"].append({
                    "language_name": language.language_name,
                    "proficiency": language.proficiency,
                    "self_evaluation": language.self_evaluation
                })
        else:
            portfolio_data["user_languages"] = "No languages added."



        if json_response:
            return jsonify(portfolio_data)
        else:
            return render_template('portfolio_logged_in.html', **portfolio_data)

    if json_response:
        return jsonify({"error": "User not logged in"})
    else:
        return render_template('portfolio_logged_out.html')

