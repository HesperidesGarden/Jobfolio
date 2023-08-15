---
title: Data Model
parent: Technical Docs
nav_order: 3
---

[Florian Eppe]
{: .label }

# Data model
{: .no_toc }
For our website "JobFolio" we focused centrally on the following functionalities in the course of our project in web development: login & registration, manage information for portfolio, manage user profile data.

The following database tables are relevant for storing the data that enable these functionalities: user, user_profile, education,language, project, skill.

The pivotal point is the table 'user': In each table there is a foreign key that refers to the primary key 'id' of the 'user' table. This ensures a 0...n relationship between 'user' and the respective other tables. That way a user can create an account without having to save any further data regarding the User-Profile and Portfolio related information. Thus ultimately allowing the user to simply create and login to an account, without having to complete the Portfolio and User-Profile related processes.

The following is a breakdown of the column names, data types, and constraints (if any) of the individual attributes of the respective database tables.# Tabelle für Login & Registration

<details open markdown="block">
<summary>- User/</summary>
<pre>
	"id"	             INTEGER PRIMARY KEY
	"first_name"	     TEXT NOT NULL,
	"last_name"	       TEXT NOT NULL,
	"email"	           TEXT UNIQUE,
	"phone_number"	   TEXT,
	"street"	         TEXT,
	"zipcode"	         TEXT,
	"city"	           TEXT,
	"password"	       TEXT  
</pre>
</details>


# Table for UserProfile

<details open markdown="block">
<summary>- User_Profile/</summary>
<pre>

  "id"                INTEGER PRIMARY KEY,
  "picture"           TEXT,
  "title"             TEXT,
  "short_description" TEXT CHECK(length("short_description") <= 500),
  "user_id"           INTEGER,
  FOREIGN KEY("user_id") REFERENCES user("id")
</pre>
</details>

# Table for Portfolio

<details open markdown="block">
<summary>- Language/</summary>
<pre>
  id I              NTEGER PRIMARY KEY,
  language_name     TEXT NOT NULL,
  proficiency       TEXT NOT NULL,
  self_evaluation   TEXT,
  user_id           INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
</pre>
</details>

<details open markdown="block">
<summary>- Project/</summary>
<pre>
  id                INTEGER PRIMARY KEY,
  title             TEXT NOT NULL,
  description       TEXT NOT NULL,
  role              TEXT,
  url_project       TEXT,
  url_picture       TEXT,
  duration          TEXT,
  difficulty        TEXT,
  user_id           INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
</pre>
</details>

<details open markdown="block">
<summary>- Skill/</summary>
<pre>
  id                INTEGER PRIMARY KEY,
  name              TEXT NOT NULL,
  proficiency       TEXT NOT NULL,
  description       TEXT NOT NULL,
  user_id           INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
</pre>
</details>

Constraints: 

'NOT NULL'-Constraints have been added throughout most of the tables to ensure a minimum amount of information, where deemed logical and sensical
