# 3MW_task
This Django project is to develop an application as shown on http://applicationtask.herokuapp.com. Moreover, Bootstrap is used as the front-end framework and the default database - sqlite3 is choosen for this project.

## Getting Started
These instructions ensure that project can be set up properly on your local machine. 
```bash
## Prerequisites (What you might need to install before running the project):
pip install -r requirements.txt

## To run the project (After cloning this Git repository, please execute the following commands):
python manage.py migrate
python manage.py loaddata sites_data
python manage.py runserver

## To use the Django Admin (Please run the following command to create a user who can login to the admin site):
python manage.py createsuperuser
##Enter your desired username and press enter.

Username: admin
##You will then be prompted for your desired email address:

Email address: admin@example.com
##The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.
```
