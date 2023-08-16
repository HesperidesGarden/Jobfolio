import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm

# chat gpt generated
db = SQLAlchemy()

def create_tables(app):
    with app.app_context():
        db.create_all()