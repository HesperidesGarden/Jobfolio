import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.usersDAO import UsersDAO
from dao.educationDAO import EducationDAO
from dao.languageDAO import LanguageDAO
from dao.projectDAO import ProjectDAO
from dao.skillDAO import SkillDAO
from project_form import project_form

def portfolio():
    if 'user_id' in session: 
        # still need portfolio DAO?
        user_profile_picture = "path/to/actual/profile_picture.jpg"
        user_name = "Jane Doe"
        user_occupation = "Digital Artist"
        user_description = "Recent art graduate with a passion for visual storytelling..."

        # fetch db stuff
        # user_projects = ProjectDAO.get_projects_by_user_id(user_id)
        # user_skills = SkillDAO.get_skills_by_user_id(user_id)
        # user_languages = LanguageDAO.get_languages_by_user_id(user_id)
    
        return render_template('portfolio_logged_in.html',
                           user_profile_picture=user_profile_picture,
                           user_name=user_name,
                           user_occupation=user_occupation,
                           user_description=user_description,
                        #  user_projects=user_projects
                        #  user_skills=user_skills,
                        #  user_languages=user_languages
                       )
        
    else:
        return render_template('portfolio_logged_out.html')
