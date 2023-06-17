CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
	address TEXT NOT NULL,
    email TEXT NOT NULL,
	phone_number TEXT
    description TEXT,
    industry TEXT,
	users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users (id)
)
CREATE TABLE education (
    id INTEGER PRIMARY KEY,
    institution TEXT NOT NULL,
    degree TEXT NOT NULL,
    field_of_study TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    description TEXT,
    users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users (id)
)
CREATE TABLE job_offers (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    requirements TEXT NOT NULL,
    location TEXT NOT NULL,
    employment_type TEXT NOT NULL,
    salary TEXT,
    working_hours TEXT,
    start_date TEXT,
    application_deadline TEXT,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(id)
)
CREATE TABLE languages (
    id INTEGER PRIMARY KEY,
    language_name TEXT NOT NULL,
    proficiency TEXT NOT NULL,
	self_evaluation TEXT,
    users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users (id)
)
CREATE TABLE messages (
  id INTEGER PRIMARY KEY,
  sender_id INTEGER NOT NULL,
  receiver_id INTEGER NOT NULL,
  message_text TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sender_id) REFERENCES users(user_id),
  FOREIGN KEY (receiver_id) REFERENCES users(user_id)
)
CREATE TABLE projects (
	id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    role TEXT,
    url_project TEXT,
	url_picture TEXT,
    duration TEXT,
    difficulty TEXT,
    users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users (id)
)
CREATE TABLE skills (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    proficiency TEXT NOT NULL,
	description TEXT NOT NULL,
    users_id INTEGER,
    FOREIGN KEY (users_id) REFERENCES users (id)
)
CREATE TABLE user_settings (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    setting_name TEXT NOT NULL,
    setting_value TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
	email TEXT UNIQUE,
    phone_number TEXT,
    address TEXT,

    password_hash TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   
)