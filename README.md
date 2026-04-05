# Codex journal
A system for tracking mythical encounters, species classifications, and combat vulnerabilities (based around the witcher 3 gameplay)

A Django web application that serves as a dynamic journal for tracking beasts, monsters, and their weaknesses. 
This project was developed as part of the Django Basics and Django Advanced courses at SoftUni.

## Live Production Site
The Witcher's Codex is currently deployed and live!
- URL: http://16.170.113.252/
- It is hosted on AWS EC2 using an Elastic IP for permanent access.
- Nginx, acting as a reverse proxy for Gunicorn.
- New registered users are automatically assigned to the 'Master Witcher' group via Django signals, granting immediate CRUD access to the Bestiary and Armory.
- To test out groups you should manually use the admin panel and assign the aprentice role to the user.


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

Provide a valid Redis URL for Celery background tasks by updating CELERY_BROKER_URL and CELERY_RESULT_BACKEND.
For example, redis://default:YOUR_REDIS_PASSWORD@YOUR_REDIS_ENDPOINT

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

To process asynchronous background tasks, open a second terminal, activate your virtual environment, and start the celery worker.

Windows:
```
celery -A codex_project worker --loglevel=info --pool=solo
```

Mac/Linux:
```commandline
celery -A codex_project worker --loglevel=info
```


## Administrative Access

To access the "Archive" (Admin Page):

URL: `http://127.0.0.1:8000/admin/` (Locally) or `http://16.170.113.252/admin/` (Live)

Access: Log in with the superuser credentials you 
made in the initialize step.

*For live version user the credentials: 
user: admin
pwd: SoftuniExamTest

## Features
Public Interface: View the home page and bestiary.

Admin Interface: Managing monster entries.

Dynamic Bestiary (CRUD): Users can create, read, update, and delete entries for various monsters.

Hunter Profile (CRUD): A personalized profile system that controls the visibility of the navigation links.

Sorting: A dropdown that allows users to sort the bestiary by Name (A-Z, Z-A) or Danger Level.

Custom Error Handling: A Witcher-themed 404 error page, as well as other error pages, for wandering travelers. 

Relational Database: Utilizes PostgreSQL with One-To-Many and Many-To-Many relationships for monster categorization and
combat vulnerabilities.

## Django Advanced Expansion
Upgrading the project to include extended user models, REST APIs, and asynchronous tasks.

- Extended User Model. Custom user authentication and role-based permissions/groups.
- Media Files Handling. Direct image uploads for monster records and hunter profiles.
- Asynchronous Processing. Celery and Redis integrated to run background tasks without blocking the server.
- RESTful APIs. Django REST Framework endpoints for external data access.
- Custom Middleware. WitcherAuditMiddleware for advanced request tracking.

## Project Structure
codex_project: The main configuration directory containing `settings.py`, `urls.py`, and the core `celery.py` setup.

accounts: Manages the custom user model, authentication logic, and role-based access/groups (Master Witcher vs. Apprentice).

common: Handles the landing page, custom error pages (404, 500), base HTML templates, global navigation, and the custom WitcherAuditMiddleware.

profiles: Manages Hunter Profile data, user biographies, and profile picture media handling.

bestiary: The core logic for monster records, threat levels, category management, combat vulnerabilities, and image handling.

quests: Handles the tracking of Witcher contracts, bounties, and task completion.

armory: Manages the weapons necessary for witchers.

tasks.py (celery): Located within the apps to handle asynchronous background operations like notifications and data exports.