**🏥 Health Management System API**


This is a simple Django REST Framework-based API for managing Clients, Programs, and Enrollments in a health organization.

It supports client registration, program enrollment, client search, and profile viewing via API endpoints.

**🚀 Features**


CRUD operations for Clients, Programs, and Enrollments.

Search for clients by first name and last name.

View a client’s full profile including programs enrolled.

Django Admin Panel fully customized with Jazzmin.

API browsable with Django REST Framework interface.

Secure JWT based login


**🛠️ Tech Stack**


Backend: Django, Django REST Framework

Admin Styling: Jazzmin

Database: db.sqlite3 (default, easy to change)


**📦 Installation**

1. Clone the repository
https://github.com/NellitG/Health.git

    cd Health

3. Create and Activate a virtual env
   
    env\Scripts\activate
4. Install dependencies

    pip install -r requirements.txt
5. Apply Migrations
   
    python manage.py migrate
6. Create superuser for admin
   
    python manage.py createsuperuser
7. Run development server
    
   python manage.py runserver

**📚 API Endpoints**

Method | Endpoint | Description

GET/POST | /api/client/ | List all clients or create a new client

GET/PUT/DELETE | /api/client/<id>/ | Retrieve, update, or delete a client

GET | /api/client/<id>/profile/ | View a client's full profile (programs enrolled)

GET/POST | /api/program/ | List all programs or create a new program

GET/POST | /api/enrollment/ | Create a new enrollment

**🔎 Admin Access**

http://127.0.0.1:8000/admin
