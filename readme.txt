- pip install Django
- pip install djangorestframework

- after installing these "cd" into JDApis
 
then 

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


then 2 endpoints will be created 

- POST http://127.0.0.1:8000/api/create/

POST using the body of JD 
eg : 
{
    "title": "Software Developer",
    "department": "Engineer",
    "industry": "Textiles",
    "description": "We are seeking a highly motivated and skilled software engineer to join our team at XYZ Company"
}




- GET http://127.0.0.1:8000/api/all/


