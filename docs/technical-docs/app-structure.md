---
title: App Structure
parent: Technical Docs
nav_order: 1
---

[Victoria-Kim Bui]
{: .label }

# App Structure

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
</details>

The structure of our web application is based on Flask, Python, and SQLAlchemy to enable efficient backend processing and database interaction. In this section, we provide an overview of the folder structure, main components, and the technologies used.

## Folder Structure

The folder structure of our application looks as follows:

<details open markdown="block">
<summary>- app/</summary>
<pre>
  - dao/
  - databasetables/
  - docs/
  - static/
  - templates/
</pre>
</details>

<details open markdown="block">
<summary>- app/databasetables/</summary>
<pre>
    - education.py
    - language.py
    - project.py
    - skill.py
    - user.py
    - userProfile.py
</pre>
</details>

<details open markdown="block">
<summary>- app/docs/</summary>
<pre>
    - assets/
    - team-eval/
      - contributions.md
      - goals.md
      - improvements.md
      - peer-review.md
      - index.md
    - technical-docs/
      - api-reference.md
      - app-behavior.md
      - app-structure.md
      - data-model.md
      - design-decisions.md
      - index.md
    - user-eval/
      - user-eval.md
    - _config.yml
    - README.md ## necessary?
    - ui-components.md ##to be deleted
    - value-proposition.md
</pre>
</details>

<details open markdown="block">
<summary>- app/static/</summary>
<pre>
    - account.css
    - edit_portfolio.css
    - findjobs.css
    - home.css
    - login.css
    - portfolio_logged_in.css
    - portfolio_logged_out.css
    - project_forms.css
    - signup.css
    - default-pfp.jpg ##own folder props
    - interview.jpg
    - logo-transperent.png
</pre>
</details>

<details open markdown="block">
<summary>- app/templates/</summary>
<pre>
    - account.html
    - findjobs.html
    - home.html
    - login.html
    - portfolio_logged_in.html
    - portfolio_logged_out.html
    - project_forms.html
    - signup.html
    - base.html
</pre>
</details>
<details open markdown="block">
<summary>- app/routes/</summary>
<pre>
    - account.py
    - portfolio.py
    - project-forms.py
    - signup.py
</pre>
</details>
- app.py
- db.py
- jobfolio.db
- LICENSE
- requirements.txt


## Main Components

Our web application is divided into various main components to ensure clear structure and reusability:

1. **Databasetables/ DAO:** The models are organized into separate modules and define the structure of the database tables. We use SQLAlchemy to abstract the database interaction.

2. **Routes Methods:** The routes methods define the used methods for the endpoints of the application and handle logic behind the HTTP requests. They are organized into separate modules to enhance maintainability.

## Used Technologies and Dependencies

Our web application utilizes various technologies and dependencies:

- **Flask:** The application is based on the Flask framework, which helps us build the web application and manage HTTP requests.

- **SQLAlchemy:** We use SQLAlchemy as an ORM (Object-Relational Mapping) to interact with the database. This simplifies database queries and manipulation.

- **bcrypt:** The bcrypt package is used for secure password hashing to ensure the security of user data.

- **Flask-Bootstrap:** Flask-Bootstrap is used to style the frontend of the application with Bootstrap elements, making the user interface appealing.

## Dependencies

Our application uses the following main dependencies (excerpt):

- **Flask:** v2.2.3
- **Flask-SQLAlchemy** v3.0.5
- **bcrypt:** v4.0.1
- **Flask-Bootstrap:** v3.3.7.1

Exact versions can be found in the `requirements.txt` file.

## Local Development

To develop the application locally, ensure that you have the dependencies installed by running `pip install -r requirements.txt`. Then use `tbd !!!!` to start the development server.
