import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobfolio.db'

db = SQLAlchemy()

def create_tables():
    with db.app.app_context():
        db.create_all()