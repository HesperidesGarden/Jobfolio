from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from databasetables.project import Project  # Annahme: Die Project-Klasse ist bereits in projects.py definiert

# connect to database
DATABASE_URL = "sqlite:///jobfolio.db"
engine = create_engine(DATABASE_URL, echo=True)

# start session
Session = sessionmaker(bind=engine)
session = Session()

class ProjectDAO:
    @classmethod
    def get_projects_by_user_id(cls, user_id):
        return session.query(Project).filter_by(users_id=user_id).all()

    @classmethod
    def create_project(cls, user_id, title, description, role, url_project, url_picture, duration, difficulty):
        new_project = Project(
            users_id=user_id,
            title=title,
            description=description,
            role=role,
            url_project=url_project,
            url_picture=url_picture,
            duration=duration,
            difficulty=difficulty
        )
        session.add(new_project)
        session.commit()
        return new_project

