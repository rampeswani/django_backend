
# Django Backend Project

This is the backend for a full-stack web application built using Django and Django REST Framework. It handles APIs, file uploads, user authentication, and integrates with Cloudinary for media storage.

---

## 📁 Project Structure

backend/

│



└── backend/ # Project config
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
├──wsgi.py
│
├── LoginUtility/ Django app
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── views.py
│ ├── urls.py

├── media/ #  Django app 
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── views.py
│ ├── urls.py

│
├── manage.py

├── README.md
├── requirements.txt
├── .gitignore




---

##  Setup Instructions



- Python 3.8+
- pip
- Git
- Virtualenv (optional but recommended)

---

###  Installation
python -m venv env
env\Scripts\activate      # For Windows
# OR
source env/bin/activate   # For Linux/macOS

# Getting the Dependency and the other packages
pip freeze > requirements.txt


# Migration Command
python manage.py migrate



# Runserver
python manage.py runserver

# Test script run command

python manage.py test --keepdb