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
2) **Create and activate virtual environment**

    ```
    python -m venv venv
    ```
Windows:
    ```
    venv\Scripts\activate
    ```

Mac/Linux:
    ```
    source venv/bin/activate
    ```

3) **Dependencies**
```
pip install -r requirements.txt
```
4) **Configuration**

This project requires a PostgreSQL database. 

Copy the .env.example file to a new file named .env.

Update the variables in .env with your local PostgreSQL 
credentials (DB_NAME, DB_USER, DB_PASSWORD).

5) **Initialize**

```
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py createsuperuser
```
Note: loaddata automatically populates the required Beast Groups and 
Combat Vulnerabilities so you can use the Bestiary immediately.

6) **Run**
```
python manage.py runserver
```
## Administrative Access

To access the "Archive" (Admin Page):

URL: `http://127.0.0.1:8000/admin/`

Access: Log in with the superuser credentials you 
made in the initialize step.

## Features
Public Interface: View the home page and bestiary.

Admin Interface: Managing monster entries.

Dynamic Bestiary (CRUD): Users can create, read, update, and delete entries for various monsters.

Hunter Profile (CRUD): A personalized profile system that controls the visibility of the navigation links.

Sorting: A dropdown that allows users to sort the bestiary by Name (A-Z, Z-A) or Danger Level.

Custom Error Handling: A Witcher-themed 404 error page for wandering travelers.

Relational Database: Utilizes PostgreSQL with One-To-Many and Many-To-Many relationships for monster categorization and
combat vulnerabilities.

## Project Structure
common: handles landing page, base templates, and global navigation.

profiles: manages Hunter Profile data and associated forms.

bestiary: core logic for monster records, category management, and combat data.