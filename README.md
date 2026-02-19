# Codex journal
A system for tracking mythical encounters, species classifications, and combat vulnerabilities (based around the witcher 3 gameplay)

A Django web application that serves as a dynamic journal for tracking beasts, monsters, and their weaknesses. 
This project was developed as part of the Django Basics course at SoftUni.

## Setup
To run the project locally, please follow these steps:

1) **Clone the repository**
```
git clone https://github.com/Yanshi04/codex-journal.git
```
2) **Dependencies**
```
pip install -r requirements.txt
```
3) **Configuration**

This project requires a PostgreSQL database. 
Please create a database named `codex_journal` and ensure your
local credentials match the following (or update settings.py):

Database Name: `codex_journal`

User: `postgres`

Password: `admin`

4) **Initialize**

```
python manage.py migrate
python manage.py createsuperuser
```
**IMPORTANT:** Because this project uses dynamic database relationships, 
you must add initial categories before creating your first Monster.
1. Run the server and navigate to `http://127.0.0.1:8000/admin`
2. Log in with your superuser credentials.
3. Add at least one item to **"Beasts groups"** (for example Cursed Ones, 
Relicts).
4. Add at least one item to **"How to wins"** (for example Silver Sword,
Steel Sword).
5. You can now return to the home page and fully use the Bestiary!


5) **Run**
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

Dynamic Bestiary (CRUD): Users can create, read, update, and delete entries for various monsters.

Hunter Profile (CRUD): A personalized profile system that controls the visibility of the navigation links.

Sorting: A dropdown that allows users to sort the bestiary by Name (A-Z, Z-A) or Danger Level.

Custom Error Handling: A Witcher-themed 404 error page for wandering travelers.

Relational Database: Utilizes PostgreSQL with One-To-Many and Many-To-Many relationships for monster categorization and
combat vulnerabilities.