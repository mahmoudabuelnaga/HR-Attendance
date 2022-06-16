[![Python 3.8.10](https://img.shields.io/badge/python-3.8.10-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.0.5](https://img.shields.io/badge/Django-4.0.5-green.svg)
![djangorestframework 3.13.1](https://img.shields.io/badge/djangorestframework-3.13.1-red.svg)
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/mahmoudabuelnaga/HR-Attendance/blob/main/LICENSE)
<!-- ![Build](https://github.com/thomas545/ecommerce_api/workflows/Django CI/badge.svg?branch=master) -->

# HR-Attendance
### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)

### Installation:

##### -> You do not need to install any kind of database

##### System Dependencies:

1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Create a virtual environment on Linux:  
`python3 -m venv venv`
4. Activate the virtual environment on Linux:
`source venv/bin/activate`
5. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`
6. Migrate Database:
`python manage.py makemigrations`
`python manage.py migrate`
7. Create Superuser
`python manage.py createsuperuser`
8. Create normal user:
`http://127.0.0.1:8000/accounts/register/`
9. Login:
`http://127.0.0.1:8000/accounts/login/`
10. List all the attendance records:
`http://127.0.0.1:8000/api/`
11. Create attendance record:
`http://127.0.0.1:8000/api/create/`


![screencapture-127-0-0-1-8000-2022-06-16-15_26_02](https://user-images.githubusercontent.com/40750581/174080206-62eabc21-fc9f-4af4-853f-b6328122af2e.png)
