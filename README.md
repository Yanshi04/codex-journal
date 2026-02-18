# Codex journal
A system for tracking mythical encounters, species classifications, and combat vulnerabilities (based around the witcher 3 gameplay)

A Django web application that serves as a dynamic journal for tracking beasts, monsters, and their weaknesses. 
This project was developed as part of the Django Basics course at SoftUni.

## Setup
To run the project locally, please follow these steps:

1) Clone the repository
```
git clone https://github.com/Yanshi04/codex-journal.git
```
2) Dependencies
```
pip install -r requirements.txt
```
3) Configuration

This project requires a PostgreSQL database. 
Please create a database named `codex_journal` and ensure your
local credentials match the following (or update settings.py):

Database Name: `codex_journal`

User: `postgres`

Password: `admin`

4) Initialize

```
python manage.py migrate
python manage.py createsuperuser
```

5) Run
```
python manage.py runserver
```
## Administrative Access

To access the "Archive" (Admin Panel):

URL: `http://127.0.0.1:8000/admin/`

Username: admin

Password: Softuni123!

## Features
Public Interface: View the home page and bestiary.

Admin Interface: Managing monster entries.