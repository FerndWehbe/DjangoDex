# DjangoDex


The purpose of the project is to train and improve my knowledge with the django framework.
In the development of the project was used:

```Python 3.10.5```
```Django 4.0.6```

The result of the project can be seen at:
[DjangoDex](https://djdex.herokuapp.com/).

## Create ```.env``` file in DjangoDex folder 
insert the django secret key inside de file.
insert the ambient type (if dont have AMBIENT variable in .env file, by default the server run in "desenv" mode and use de sqlite as your data base)

##### ```.env``` file example:
```
    DJANGO_SECRET=your_django_secret_key
```


##### If running in lunix or unix and use postgres-sql:
Install ```python3-dev libpq-dev``` and install python module ```psycopg2```

More infos in [Django-docs#postgresql](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes).

## Installation
### For easiest deploy you can use de makefile. 
First you need create a virtualenv and load that.

**Create python virtualenv**
```python -m venv venv```
or 
 ```python3 -m venv venv```

**Load venv**

Windows
```./venv/Script/activate```

Linux
```source venv/bin/activate```

**After loaded virtualenv use**

```make deploy```

This command goes install all dependences, load the migrates, import all dex data in database and start django web server.

You can do it step by step using:

Command               | Result
----------------------|-------
 ```make install```    | for install dependences
 ```make migrate```    | for make migrations in database
 ```make loaddata```   | for insert all dex data in database
 ```make run```        | for start django server in localhost with port 8000

*Bonus:*
* *```make createuser```   help you create a superuser for acess admin page and manage all data in models.*



>### django-tailwind
> The project uses the tailwind CSS library to style the pages. To help with the library configuration installation processor I used the django-tailwind module.
>
> Read the docs for more info.
> [Django Tailwind Usage - Tutorial](https://django-tailwind.readthedocs.io/en/latest/installation.html).
 