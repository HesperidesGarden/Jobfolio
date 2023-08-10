import os
from flask import Flask, session, render_template, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dao.UsersDAO import UsersDAO
from dao.EducationDAO import EducationDAO
from dao.LanguageDAO import LanguageDAO
from dao.ProjectDAO import ProjectDAO
from dao.SkillDAO import SkillDAO
from dao.UserProfileDAO import UserProfileDAO
from project_form import project_form

def portfolio():
    if 'user_id' in session: 
        user_id = session['user_id']
        
        user_name = UsersDAO.get_user_full_name(user_id)
        user_profile_picture = UserProfileDAO.get_user_profile_picture(user_id)
        user_occupation = UserProfileDAO.get_user_occupation(user_id)
        user_description = UserProfileDAO.get_user_description(user_id)

        # fetch db stuff
        #user_projects = ProjectDAO.get_projects_by_user_id(user_id)
        #user_skills = SkillDAO.get_skills_by_user_id(user_id)
        #user_languages = LanguageDAO.get_languages_by_user_id(user_id)
    
        return render_template('portfolio_logged_in.html',
                        user_profile_picture=user_profile_picture,
                        user_name=user_name,
                        user_occupation=user_occupation,
                        user_description=user_description,
                        #user_projects=user_projects,
                        #user_skills=user_skills,
                        #user_languages=user_languages
                        )
        
    else:
        return render_template('portfolio_logged_out.html')
    
