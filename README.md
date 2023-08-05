# franco_fitness_api

## Getting Started

App created from Django REST Framework quickstart tutorial: https://www.django-rest-framework.org/tutorial/quickstart/
To run the app locally, create a Python virtual environment to isolate package dependencies locally:

```
python -m venv env
source env/bin/activate
```

Windows:
```
python -m venv env
source env\Scripts\activate
```

Note: To exit the virtual environment at any time, just type `deactivate`


Install relevant libraries into the virtual environment:
```
pip install django
pip install djangorestframework
pip install mysqlclient
pip install python-dotenv
```

## Available scripts
To run migration:
```
python manage.py migrate
```

To run the server:
```
python manage.py runserver
```


Changes to migration:
```
python manage.py makemigrations
```