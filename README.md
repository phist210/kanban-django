<<<<<<< HEAD
# Trello Clone

Here we build a clone of the well known project-management application using Django Rest Frameworks,
=======
# Kanban Django

Here we build a clone of the well known project-management application, Trello using Django Rest Frameworks,
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed
Javascript, Ajax and HTML/CSS.


#### Prerequisites

* [PostgreSQL](https://www.postgresql.org/download/) - An open source object-relational database system
* [Postico](https://eggerapps.at/postico/) - A Modern PostgreSQL Client for OSX

Python3

```
pip install python3
```

Additional python libraries needed to run this project

```
pip install -r requirements.txt
```


### Installing

After cloning or downloading this repo, change the settings.py to satisfy your personal specs:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<[your database name]>',
        'USER': '<[your username]>',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Next, create a new database in Postico that matches the name used in the settings.py.

From manager directory execute:

```
python manage.py migrate
```

Then execute:

```
python manage.py runserver
```

and navigate to [Home Page](http://localhost:8000/kanban/)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Authors

* **Josh Friese** - *Initial work* - [phist210](https://github.com/phist210/)
* **Luis Garcia** - *Initial work* - [emanonGarcia](https://github.com/emanongarcia)
