import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.userDAO import UserDAO
from dao.educationDAO import EducationDAO
from dao.languageDAO import LanguageDAO
from dao.projectDAO import ProjectDAO
from dao.skillDAO import SkillDAO
from dao.userProfileDAO import UserProfileDAO
from project_form import project_form

def portfolio():
    user_dao = UserDAO()
    education_dao = EducationDAO()
    language_dao = LanguageDAO()
    project_dao = ProjectDAO()
    skill_dao = SkillDAO()
    userProfile_dao = UserProfileDAO()
    
    if 'user_id' in session: 
        user_id = session['user_id']
        
        user_name = user_dao.get_user_full_name(user_id)
        user_profile_picture = userProfile_dao.get_user_profile_picture(user_id)
        user_occupation = userProfile_dao.get_user_occupation(user_id)
        user_description = userProfile_dao.get_user_description(user_id)

        # fetch db stuff
        #user_projects = ProjectDAO.get_projects_by_user_id(user_id)
        user_skills = skill_dao.get_skills_by_user_id(user_id)
        user_languages = language_dao.get_languages_by_user_id(user_id)
    
        return render_template('portfolio_logged_in.html',
                        user_profile_picture=user_profile_picture,
                        user_name=user_name,
                        user_occupation=user_occupation,
                        user_description=user_description,
                        #user_projects=user_projects,
                        user_skills=user_skills,
                        user_languages=user_languages
                        )
        
    else:
        return render_template('portfolio_logged_out.html')
    
