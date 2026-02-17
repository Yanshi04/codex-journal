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
3) Run
```
python manage.py runserver
```
(Note: The project includes a pre-configured SQLite database with test data!)

## Administrative Access

To access the "Archive" (Admin Panel):

URL: `http://127.0.0.1:8000/admin/`

Username: admin

Password: Softuni123!

## Features
Public Interface: View the home page and bestiary.

Admin Interface: Managing monster entries.