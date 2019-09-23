1. Create a folder called DjangoProjects in the Centos Linux Desktop

```
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ ls
[kuvivek@vivekcentos DjangoProjects]$
```

2. Since Centos7 comes default with python2.7. Hence for using the newer 
Python3.7. Perform the build of Python3.7 source code and install it in
another location.
 

```
[kuvivek@vivekcentos ~]$
[kuvivek@vivekcentos ~]$ python
Python 2.7.5 (default, Aug  7 2019, 00:51:29)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> exit()
[kuvivek@vivekcentos ~]$
[kuvivek@vivekcentos ~]$ which python
/usr/bin/python
[kuvivek@vivekcentos ~]$
[kuvivek@vivekcentos ~]$ which python3.7
/usr/local/bin/python3.7
[kuvivek@vivekcentos ~]$
[kuvivek@vivekcentos ~]$
```

3. Before starting any Django project, It is advisable to create a virtualenv.
If we execute the command like this It will create python2.7 Virtualenv
which we obviously don't want.

```
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ virtualenv MyMDB
  No LICENSE.txt / LICENSE found in source
New python executable in /home/kuvivek/Desktop/DjangoProjects/MyMDB/bin/python2
Also creating executable in /home/kuvivek/Desktop/DjangoProjects/MyMDB/bin/python
Installing setuptools, pip, wheel...
done.
[kuvivek@vivekcentos DjangoProjects]$
```

So the solution to create virtualenv with python3. It need the following steps.

3.1 Creating My Movie Database folder in short 'MyMDB' using the below command 


```
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ python3.7 -m virtualenv MyMDB
/usr/local/bin/python3.7: No module named virtualenv
[kuvivek@vivekcentos DjangoProjects]$
```

3.2 The `virtualenv` command itself was not available in Python3.7. So 
It is required to install `virtualenv` first.
 
```
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ python3.7 -m pip install virtualenv
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/8b/12/8d4f45b8962b03ac9efefe5ed5053f6b29334d83e438b4fe379d21c0cb8e/virtualenv-16.7.5-py2.py3-none-any.whl (3.3MB)
     |████████████████████████████████| 3.3MB 58kB/s
Installing collected packages: virtualenv
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.7/site-packages/virtualenv.py'
Consider using the `--user` option or check the permissions.

[kuvivek@vivekcentos DjangoProjects]$
```

3.3 Since the python is installed in the current user context. It is advising 
to run the same with --user option. Although the package is cached but failed
to install in the site-packages folder.


```
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ python3.7 -m pip install virtualenv --user
Collecting virtualenv
  Using cached https://files.pythonhosted.org/packages/8b/12/8d4f45b8962b03ac9efefe5ed5053f6b29334d83e438b4fe379d21c0cb8e/virtualenv-16.7.5-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-16.7.5
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ python3.7 -m virtualenv MyMDB
Using base prefix '/usr/local'
New python executable in /home/kuvivek/Desktop/DjangoProjects/MyMDB/bin/python3.7
Also creating executable in /home/kuvivek/Desktop/DjangoProjects/MyMDB/bin/python
Installing setuptools, pip, wheel...
done.
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$
```

3.4 Virtual environment MyMDB is created. It need to be activated.

```
[kuvivek@vivekcentos DjangoProjects]$ ls
MyMDB  README.md
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$ source MyMDB/bin/activate
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ python
Python 3.7.3 (default, Sep  1 2019, 17:16:31)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> exit()
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
```

4. Create a requirements.dev.txt file so as to install necessary softwares. Currently only the python3 is installed.

```
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ vi requirements.dev.txt
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ cat requirements.dev.txt
django<2.1
psycopg2<2.8
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ pip install -r requirements.dev.txt
Collecting django<2.1 (from -r requirements.dev.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/67/b0/64645bd6c5cdabb07d361e568eecfa9e64027ae4cb4778bb00be8c4bde00/Django-2.0.13-py3-none-any.whl (7.1MB)
     |████████████████████████████████| 7.1MB 39kB/s
Collecting psycopg2<2.8 (from -r requirements.dev.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/0c/ba/e521b9dfae78dc88d3e88be99c8d6f8737a69b65114c5e4979ca1209c99f/psycopg2-2.7.7-cp37-cp37m-manylinux1_x86_64.whl (2.7MB)
     |████████████████████████████████| 2.7MB 10.0MB/s
Collecting pytz (from django<2.1->-r requirements.dev.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/87/76/46d697698a143e05f77bec5a526bf4e56a0be61d63425b68f4ba553b51f2/pytz-2019.2-py2.py3-none-any.whl
Installing collected packages: pytz, django, psycopg2
Successfully installed django-2.0.13 psycopg2-2.7.7 pytz-2019.2
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
```

5. Now Django is installed for this virtual environment.
Lets create a project called config.

```
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ django-admin startproject config
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ tree config/
config/
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 5 files
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
```

6. Moving the project name to django from config.

```
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ mv config django
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ tree django
django
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 5 files
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$
```

7. Configuring Database Settings. 
Since by default the Django uses by default SQLITE DB, which is not suitable for Production. 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

As a matter of best practice change it to the same PostgresSQL DB for development also.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mymdb',
        'USER': 'mymdb',
        'PASSWORD': 'development',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

8. Create an app inside the `django` project folder formerly `config` folder, using startapp command shown below:

```
(MyMDB) [kuvivek@vivekcentos django]$ tree .
.
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 5 files
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py startapp core
/home/kuvivek/Desktop/DjangoProjects/MyMDB/lib/python3.7/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ tree
.
├── config
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── settings.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py

4 directories, 14 files
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ pip install psycopg2-binary
Collecting psycopg2-binary
  Using cached https://files.pythonhosted.org/packages/f3/21/b7ccc8ae35e5b6ae62bfe47181353628bae52489c7798f00efd7916de543/psycopg2_binary-2.8.3-cp37-cp37m-manylinux1_x86_64.whl
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.8.3
(MyMDB) [kuvivek@vivekcentos django]$
```

9. Now In the `settings.py` of the config folder `INSTALLED_APPS`, which is a 
list of Python paths to Python modules that are Django apps. These apps are by
default installed to solve common problems, such as managing static files,
sessions, and authentication and an admin backend.
So Lets put our core app in this.

```
INSTALLED_APPS = [
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
10. Adding First Model - Movie

```
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ cat core/models.py
from django.db import models

class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G,
         'G - General Audiences'),
        (RATED_PG,
         'PG - Parental Guidance '
         'Suggested'),
        (RATED_R, 'R - Restricted'),
    )

    title = models.CharField(
        max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices=RATINGS,
        default=NOT_RATED)
    runtime = \
        models.PositiveIntegerField()
    website = models.URLField(
        blank=True)

    def __str__(self):
        return '{} ({})'.format(
            self.title, self.year)

(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$
```


11. Migrating the Database

Since the Model is created now, It's the time to create a table that matches the 

While Django can create and run migrations for our Django apps, it will not create the
database and database user for our Django project. To create the database and user, we have
to connect to the server using an administrator's account. Once we've connected we can
create the database and user by executing the following SQL:


```
[kuvivek@vivekcentos DjangoProjects]$ su - postgres
Password:
Last login: Thu Sep 12 13:49:19 EDT 2019 on pts/0
-bash-4.2$
-bash-4.2$
-bash-4.2$ psql postgres
psql (9.2.24)
Type "help" for help.

postgres=#
postgres=# \l
                                  List of databases
    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
------------+----------+----------+-------------+-------------+-----------------------
 mydatabase | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
 template1  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
(4 rows)

postgres=# create database mymdb;
CREATE DATABASE
postgres=#
postgres=# create user mymdb;
CREATE ROLE
postgres=#
postgres=# grant all on database mymdb to "mymdb";
GRANT
postgres=#
postgres=# alter user mymdb password 'development';
ALTER ROLE
postgres=#
postgres=# alter user mydb createdb;
ERROR:  role "mydb" does not exist
postgres=#
postgres=# alter user mymdb createdb;
ALTER ROLE
postgres=#
postgres=#
postgres-#
postgres-# \q
-bash-4.2$
-bash-4.2$ exit
logout
[kuvivek@vivekcentos DjangoProjects]$
[kuvivek@vivekcentos DjangoProjects]$
```

The above SQL statements will create the database and user for our Django project. The
'grant' statement ensures that our mymdb user will have access to the database. Then, we
set a password on the `mymdb` user (make sure it's the same as in your `settings.py` file).
Finally, we give the `mymdb` user permission to create new databases, which will be used by
Django to create a test database when running tests.

12. 

To generate a migration for our app, we'll need to tell `manage.py` file to do as follows:

```
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py makemigrations core
Migrations for 'core':
  core/migrations/0001_initial.py
    - Create model Movie
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$
```

A migration is a Python file in our Django app that describes how to change the database
into a desired state. Django migrations are not tied to a particular database system (the
same migrations will work across supported databases, unless we add database-specific
code). Django generates migration files that use Django's migrations API.

Remember that it's apps not projects that have migrations (since it's apps that have models).
Next, we tell `manage.py` to migrate our app:

```
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py migrate core
Operations to perform:
  Apply all migrations: core
Running migrations:
  Applying core.0001_initial... OK
(MyMDB) [kuvivek@vivekcentos django]$
```

Now, our table exists in our database:

```
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py dbshell
psql (9.2.24)
Type "help" for help.

mymdb=>
mymdb=> \dt
             List of relations
 Schema |       Name        | Type  | Owner
--------+-------------------+-------+-------
 public | core_movie        | table | mymdb
 public | django_migrations | table | mymdb
(2 rows)

mymdb=>
mymdb=> \q
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$
```

We can see that our database has two tables. The default naming scheme for Django's
model's tables is <app_name>_<model_name>. We can tell `core_movie` is the table for the
`Movie` model from the `core` app. `django_migrations` is for Django's internal use to track
the migrations that have been applied. Altering the `django_migrations` table directly
instead of using `manage.py` is a bad idea, which will lead to problems when you try to
apply or roll back migrations.

The migration commands can also run without specifying an app, in which case it will run
on all the apps. Let's run the `manage.py` command without an app:

```
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$
```

This creates tables to keep track of users, sessions, permissions, and the administrative
backend.

13. Creating our First Movie.

Like Python, Django offers an interactive REPL to try things out. The Django shell is fully
connected to the database, so we can create, query, update, and delete models from the
shell:

```
(MyMDB) [kuvivek@vivekcentos django]$
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py shell
Python 3.7.3 (default, Sep  1 2019, 17:16:31)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
>>>
>>> from core.models import Movie
>>> sleuth = Movie.objects.create(
... title='Sleuth',
... plot='An snobbish writer who loves games'
... ' invites his wife\'s lover for a battle of wits.',
... year=1972,
... runtime=138,
... )
>>>
>>> sleuth.id
1
>>> sleuth.get_rating_display()
'NR - Not Rated'
>>>
>>> exit()
(MyMDB) [kuvivek@vivekcentos django]$
```

Next, let's create a backend for managing movies using the Django Admin app.

14. Creating Movie Admin
 
To get Django's admin app working with our models, we will perform the following steps:
  1. Register our model
  2. Create a super user who can access the backend
  3. Run the development server
  4. Access the backend in a browser

Registering Movie Model with the admin by editing `django/core/admin.py` file.

```
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ cat django/core/admin.py 
from django.contrib import admin

# Register your models here.

from core.models import Movie

admin.site.register(Movie)
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ 

```

Once the Movie model is registered, then Create a super user.

```
(MyMDB) [kuvivek@vivekcentos django]$ 
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py createsuperuser
Username (leave blank to use 'kuvivek'): 
Email address: vivekkumar.bitsindri@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(MyMDB) [kuvivek@vivekcentos django]$ 
(MyMDB) [kuvivek@vivekcentos django]$ 
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 22, 2019 - 21:47:05
Django version 2.0.13, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


15. Creating MovieList view
When Django gets a request, it uses the path of the request and the `URLConf` of the project
to match a request to a view, which returns an HTTP response. Django's views can be either
functions, often referred to as Function-Based Views (FBVs), or classes, often called Class-
Based Views (CBVs). The advantage of CBVs is that Django comes with a rich suite of generic 
views that you can subclass to easily (almost declaratively) write views to accomplish common
tasks.

Let's write a view to list the movies that we have. Open `django/core/views.py` and
change it to the following:

```
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ 
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ cat django/core/views.py 
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from core.models import Movie

class MovieList(ListView):

    # ListView requires atleast a model attribute, Hence added the same below.
    # It will query for all the rows of that model, pass it to the template
    # and returned the rendered template in a response.
    model = Movie

(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ 

```

`ListView` requires at least a `model` attribute. It will query for all the rows of that model,
pass it to the template, and return the rendered template in a response. It also offers a
number of hooks that we may use to replace default behavior.

How does `ListView` know how to query all the objects in `Movie`? For that, we will need to
discuss manager and `QuerySet` classes. Every model has a default manager. Manager classes are 
primarily used to query objects by offering methods, such as `all()`, that return a `QuerySet`. 
A `QuerySet` class is Django's representation of a query to the database. `QuerySet` has a 
number of methods, including `filter()` (such as a 'WHERE' clause in a 'SELECT' statement) to
limit a result. One of the nice features of the `QuerySet` class is that it is lazy; it is not
evaluated until we try to get a model out of the `QuerySet`. Another nice feature is that 
methods such as `filter()` take lookup expressions, which can be field names or span across
relationship models.

So, how does `ListView` know that it has to query all the objects in `Movie`? `ListView`
checks whether it has a `model` attribute, and, if present, knows that `Model` classes have a
default manager with a `all()` method, which it calls. `ListView` also gives us a convention
for where to put our template, as follows: `<app_name><model_name>_list.html`.

16. Adding our first template - movie_list.html

Django ships with its own template language called the Django Template language.
Django can also use other template languages (for example, Jinja2), but most Django
projects find using the Django Template language to be efficient and convenient.
In the default configuration that is generated in our `settings.py` file, the Django Template
language is configured to use "APP_DIRS" , meaning that each Django app can have a
`templates` directory, which will be searched to find a template. This can be used to
override templates that other apps use without having to modify the third-party apps
themselves.

Let's make our first template in `django/core/templates/core/movie_list.html`.

The final step will be to connect our view to a `URLConf`.


17. Routing requests to our view with URLConf

Now that we have a model, view, and template, we will need to tell Django which requests
it should route to our `MovieList` View using a URLConf. Each new project has a root
URLConf that created by Django (in our case it's the `django/config/urls.py` file).
Django developers have developed the best practice of each app having its own URLConf.
Then, the root URLConf of a project will include each app's URLConf using the `include()`
function.

create a URLConf for our core app by creating a `django/config/urls.py` file.
And then connect our `URLConf` to the root `URLConf` by changing `django/config/urls.py`.


