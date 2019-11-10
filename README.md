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

18. Creation of Individual movie page

To add movie details following things are required.
  
  1. Create a movie detail view
  2. Create a movie_detail.html template
  3. Reference to our MovieDetail view in our URLConf


  18.1 Django provides DetailView class that we can subclass to create a view showing the details of single 
       Model.   
   
  Create view in django/core/views.py

```   
@@ -1,7 +1,7 @@
 from django.shortcuts import render
 
 # Create your views here.
-from django.views.generic import ListView
+from django.views.generic import ListView, DetailView
 
 from core.models import Movie
 
@@ -12,3 +12,5 @@ class MovieList(ListView):
     # and returned the rendered template in a response.
     model = Movie
 
+class MovieDetail(DetailView):
+    model = Movie
(MyMDB) [kuvivek@vivekcentos DjangoProjects]$ 

```   
   18.2 Create movie_detail.html template

Django's Template language supports template inheritance, which means that you can write
a template with all the look and feel for our website and mark the `block` sections that
other templates will override. This allows to create the look and feel of the entire website
without having to edit each template. Creating a base template with MyMDBb's branding and
look and feel and then add a Movie Detail template that inherits from the
base template.

A base template shouldn't be tied to a particular app, so let's make a general templates
directory:

 `$ mkdir django/templates`

Django doesn't know to check our `templates` directory yet, so we will need to update the
configuration in our `settings.py` file. Find the line that starts with `TEMPLATES` and
change the configuration to list our `templates` directory in the `DIRS` list:

```   
@@ -55,7 +55,9 @@ ROOT_URLCONF = 'config.urls'
 TEMPLATES = [
     {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
-        'DIRS': [],
+        'DIRS': [
+           os.path.join(BASE_DIR, 'templates'),
+        ],
         'APP_DIRS': True,
         'OPTIONS': {
             'context_processors': [

```   

Let's create a base template in django/templates/base.html that has a main column and sidebar.

```   
<!DOCTYPE html>
<html lang="en" >
<head >
  <meta charset="UTF-8" >
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1, shrink-to-fit=no"
  >
  <link
    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css"
    integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M"
    rel="stylesheet"
    crossorigin="anonymous"
  >
  <title >
    {% block title %}MyMDB{% endblock %}
  </title>
  <style>
    .mymdb-masthead {
      background-color: #EEEEEE;
      margin-bottom: 1em;
    }
  </style>

</head >
<body >
<div class="mymdb-masthead">
  <div class="container">
    <nav class="nav">
      <div class="navbar-brand">MyMDB</div>
      <a
        class="nav-link"
        href="{% url 'core:MovieList' %}"
      >
        Movies
      </a>
    </nav>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-sm-8 mymdb-main">
     {% block main %}{% endblock %}
    </div>
    <div
        class="col-sm-3 offset-sm-1 mymdb-sidebar"
    >
      {% block sidebar %}{% endblock %}
    </div>
  </div>
</div>

</body >
</html >

```   

Most of this HTML is actually bootstrap (HTML/CSS framework) boilerplate, but we do
have a few new Django tags:

`{% block title %}MyMDB{% endblock %}` : This creates a block that other templates 
can replace. If the block is not replaced, the contents from the parent template will 
be used.


href="{% url 'core:MovieList' %}" : The `url` tag will produce a URL path
for the named `path` . URL names should be referenced as `<app_namespace>:<name>`; in our 
case, `core` is the namespace of the core app (per `django/core/urls.py`), and `MovieList` 
is the name of the MovieList view's URL.

This lets us create a simple template in `django/core/templates/core/movie_detail.html`

```   
{% extends 'base.html' %}

{% block title %}
  {{ object.title }} - {{ block.super }}
{% endblock %}

{% block main %}
<h1>{{ object }}</h1>
<p class="lead">
{{ object.plot }}
</p>
{% endblock %}

{% block sidebar %}
<div>
This movie is rated:
  <span class="badge badge-primary">
  {{ object.get_rating_display }}
  </span>
</div>
{% endblock %}

```   

Let's take a look at some new tags:

`{% extends 'base.html' %}` : If a template wants to extend another template
the first line must be an `extends` tag. Django will look for the base template
(which can `extend` another template) and execute it first, then replace the blocks.
A template that extends another cannot have content outside of blocks because
it's ambiguous where to put that content.

`{{ object.title }} - {{ block.super }}` : We reference `block.super`
inside the `title` template block. `block.super` returns the contents of the
`title` template `block` in the base template.

`{{ object.get_rating_display }}` : The Django Template language doesn't
use () to execute the method, just referencing it by name will execute the
method.

 18.3 Adding MovieDetail to core/urls.py 

```
@@ -6,5 +6,6 @@ app_name = 'core'
 
 urlpatterns = [
   path('movies', views.MovieList.as_view(), name='MovieList'),
+  path('movies/<int:pk>', views.MovieDetail.as_view(), name='MovieDetail'),
 
 ]

```

The `MovieDetail` and `MovieList` both calls `path()` which look almost the same, except 
for the `MovieDetail` string that has a named parameter. A path route string can include angle
brackets to give a parameter a name and even define a type that the parameter's content must 
conform to (for example, int:pk will only match values that parse as an int ). These named 
sections are captured by Django and passed to the view by name. DetailView expects a pk	(or slug) 
argument and uses it to get the correct row from the database.

A slug is a short URL-friendly label that is often used in content-heavy sites, as it
is SEO friendly.


Let's use `python manage.py runserver` to start the `dev` server and take a 
look at what our new template looks like:


```
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 28, 2019 - 22:42:17
Django version 2.0.13, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[28/Sep/2019 22:43:47] "GET /movies HTTP/1.1" 200 210
[28/Sep/2019 22:44:22] "GET /movies HTTP/1.1" 200 210
[28/Sep/2019 22:44:27] "GET /movies/1 HTTP/1.1" 200 1263
[28/Sep/2019 22:44:32] "GET /movies HTTP/1.1" 200 210
[28/Sep/2019 22:44:37] "GET /movies/2 HTTP/1.1" 200 1271
[28/Sep/2019 22:44:41] "GET /movies/1 HTTP/1.1" 200 1263

```

19. Pagination and Linking MovieList view to MovieDetail view

Lets add pagination in the `MovieList` view to prevent it from querying the 
entire database each time.

This needs updation of MovieList.html to extend the base.html.

```
@@ -1,16 +1,18 @@
-<!DOCTYPE html>
-<html>
-  <body>
-    <ul>
-      {% for movie in object_list %}
-        <li>{{ movie }}</li>
-      {% empty %}
-        <li> No Movies yet.</li>
-      {% endfor %}
-    </ul>
-    <p>
-      Using https?
-      {{ request.is_secure|yesno }}
-    </p>    
-  </body>
-</html>
+{% extends 'base.html' %}
+
+{% block title %}
+All the Movies
+{% endblock %}
+
+{% block main %}
+<ul>
+  {% for movie in object_list %}
+    <li>
+      <a href="{% url 'core:MovieDetail' pk=movie.id %}">
+        {{ movie }}
+      </a>
+    </li>
+  {% endfor %}
+</ul>
+{% endblock %}
+

```

Here with the `url` tag, the `MovieDetail` URL requires a `pk` argument. 
If there was no argument provided, then Django would raise a `NoReverseMatch` 
exception on rendering, resulting in a 500 error.

20. Setting the Page Order.

Another problem with our current view is that it's not ordered. If the database is returning
an unordered query, then pagination won't help navigation. What's more, there's no 
guarantee that each time the user changes pages that the content will be consistent, as the
database may return a differently ordered result set for each time. It is required that the 
query to be ordered consistently.
Ordering our model also makes our lives as developers easier too. Whether using a debugger, 
writing tests, or running a shell ensuring that our models are returned in a consistent order 
can make troubleshooting simpler. A Django model may optionally have an inner class called `Meta`
, which lets us specify information about a Model. Let's add a `Meta` class with an `ordering` attribute:


```
@@ -19,6 +19,9 @@ class Movie(models.Model):
     runtime = models.PositiveIntegerField()
     website = models.URLField(blank = True)
 
+    class Meta:
+        ordering = ('-year', 'title')
+
     def __str__(self):
         return '{} ({})'.format(
             self.title, self.year)

```

`ordering` takes a list or tuple of, usually, strings that are field names, optionally prefixed
by a `-` character that denotes descending order. ('-year', 'title') is the equivalent of
the SQL clause `ORDER BY year DESC, title`.

Adding `ordering` to a Model's `Meta` class will mean that `QuerySets` from the model's
manager will be ordered.


21. Adding Pagination

Now that our movies are always ordered the same way, let's add pagination. A Django
`ListView` already has built-in support for pagination, so all we need to do is take
advantage of it. Pagination is controlled by the `GET` parameter `page` that controls which
page to show.

Let's add pagination to the bottom of our `main` template `block` :

Add the below code into the core/templates/core/movie_list.html

```
{% block main %}
<ul>
  {% for movie in object_list %}
    <li>
      <a href="{% url 'core:MovieDetail' pk=movie.id %}">{{ movie }}</a>
    </li>
  {% endfor %}
</ul>
{% if is_paginated %}
    <nav >
      <ul class="pagination" >
        <li class="page-item" >
          <a href="{% url 'core:MovieList' %}?page=1" class="page-link" >First</a >
        </li >
        {% if page_obj.has_previous %}
          <li class="page-item" >
            <a href="{% url 'core:MovieList' %}?page={{ page_obj.previous_page_number }}" class="page-link" >{{ page_obj.previous_page_number }}</a >
          </li >
        {% endif %}
        <li class="page-item active" >
          <a href="{% url 'core:MovieList' %}?page={{ page_obj.number }}" class="page-link" >{{ page_obj.number }}</a >
        </li >
        {% if page_obj.has_next %}
          <li class="page-item" >
            <a href="{% url 'core:MovieList' %}?page={{ page_obj.next_page_number }}" class="page-link" >{{ page_obj.next_page_number }}</a >
          </li >
        {% endif %}
        <li class="page-item" >
          <a href="{% url 'core:MovieList' %}?page=last" class="page-link" >Last</a >
        </li >
      </ul >
    </nav >
{% endif %}
{% endblock %}
```

Let's take a look at some important points of our `MovieList` template:
* `page_obj` is of the `Page` type, which knows information about this page of results. We use it to check whether there is a next/previous page using
`has_next()` / `has_previous()` (we don't need to put in the Django template language, but `has_next()` is a method, not a property). We also use it to get
the `next_page_number()`/ `previous_page_number()`. Note that it is important to use the `has_*()`  method to check for the existence of the next/previous page
numbers before retrieving them. If they don't exist when retrieved, `Page` throws an `EmptyPage` exception.

`object_list` continues to be available and hold the correct values. Even though `page_obj` encapsulates the results for this page in `page_obj.object_list`, 
`ListView` does the convenient work of ensuring that we can continue to use `object_list` and our template doesn't break.

22. 404 - Error page when the sought URL doesn't exist.

We now have a couple of views that can't function if given the wrong value in the URL (the wrong `pk` will break `MovieDetail`; the wrong `page` will break `MovieList` ); 
let's plan for that by handling  errors. Django offers a hook in the root URLConf to let us use a custom view for 404 errors (also for 403, 400 , and 500 all following 
the same names scheme). In your root `urls.py` file, add a variable called `handler404` whose value is a string Python path to your custom view.
However, we can continue to use the default  handler view and just write a custom template. Let's add a  template in `django/template/404.html`.

Even if another app throws a 404 error, this template will be used.

At the moment, if you've got an unused URL such as `http://localhost:8000/unreal-page`, you won't see our custom 404 template
because Django's `DEBUG` settings is `True` in `settings.py`. To make our 404 template visible, we will need to change the `DEBUG` and `ALLOWED_HOSTS` settings in `settings.py` :
   `DEBUG = False`
   `ALLOWED_HOSTS = [
      'localhost',
      '127.0.0.1'
    ]`

`ALLOWED_HOSTS` is a setting that restricts which `HOST` values in an HTTP request Django will respond to. If `DEBUG` is `False` and a `HOST` does not match an `ALLOWED_HOSTS` value,
then Django will return a 400 error (you can customize both the view and template for this error as described in the preceding code). 

With the following changes. The customized Page can be tested by putting the following URL in the browser.

`http://127.0.0.1:8000/unreal-page`

23. Testing Views and Templates

The basics of testing is simple. The common XUnit pattern of the `TestCase` classes holding test methods that make assertions.

For Django's TestRunner to find a test, it must be in the `tests` module of an installed app. That means `tests.py`.

Adding the following testcase to perform TDD (Test Driven development).
  - If there is more than 10 movies, then pagination controls should be rendered in the template.
  - If there is more than 10 movies and we don't provide `page GET` parameters, consider the following things.
     - The page_is_last context variable should be False.
     - The page_is_first context variable should be True.
     - The first item in the pagination should be marked as active.


The following is our test.py file in 

```    
(MyMDB) [kuvivek@vivekcentos core]$ cat tests.py 
from django.test import TestCase

# Create your tests here.

from django.test.client import RequestFactory
from django.urls.base import reverse

from core.models import Movie
from core.views import MovieList


class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
      <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Movie.objects.create(title='Title {}'.format(n), year=1990 + n,
                runtime=100,)

    def testFirstPage(self):
        movie_list_path = reverse('core:MovieList')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(self.ACTIVE_PAGINATION_HTML.format(
                movie_list_path, 1, 1),
            response.rendered_content)
(MyMDB) [kuvivek@vivekcentos core]$ 

```    

Some interesting points with the TestCases.

  a) `class MovieListPaginationTestCase(TestCase)`: `TestCase` is the base class for all Django tests. It has a number of convenient assert methods.

  b) `def setUp(self)`: Like most XUnit testing frameworks, Django's TestCase
class offers a `setUp()` hook that is run before each test. A `tearDown()` hook is also available if needed. The database is cleaned up between each test, so we
don't need to worry about deleting any models we added.
  
  c) `def testFirstPage(self)`: A method is a test if its name is prefixed with test.

  d) `movie_list_path = reverse('core:MovieList')`: `reverse()` is the Python equivalent of the url Django template tag. It will resolve the name into a path.

  e) `request = RequestFactory().get(path=movie_list_path)`: RequestFactory is aconvenient factory for creating fake HTTP requests. A RequestFactory has convenience methods for creating GET,POST, and PUT requests by its convenience methods named after the verb (for example, get() for GET requests). In our case, the path object provided doesn't matter, but other views may want to inspect the path of the request.

  f) `self.assertEqual(200, response.status_code)`: This asserts that the two arguments are equal. A response's status_code to check success or failure (200 being the status code for success - The one code you never see when you browse the web). 

  g) `self.assertTrue(response.context_data['is_paginated'])`: This asserts that the argument evaluates to True. response exposes the context that is used in rendering the template. This makes finding bugs much easier as you can quickly check actual values used in rendering.

  h) `self.assertInHTML(` : `assertInHTML` is one of the many convenient methods that Django provides as part of its Batteries Included philosophy. Given a valid HTML string `needle` and valid HTML string `haystack`, it will assert that `needle` is in `haystack`.

To run the tests, we can use `manage.py`.

(MyMDB) [kuvivek@vivekcentos django]$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: testFirstPage (core.tests.MovieListPaginationTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kuvivek/Desktop/DjangoProjects/django/core/tests.py", line 29, in testFirstPage
    self.assertTrue(response.context_data['is_paginated'])
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.031s

FAILED (failures=1)
Destroying test database for alias 'default'...
(MyMDB) [kuvivek@vivekcentos django]$ 

It failed. May be in one page all the movie details are able to adjust. In order to simulate the pagination, Lets force the list view to display two movies per page.
In order to achieve the same. Lets add the following attribute in the class MovieList

```
(MyMDB) [kuvivek@vivekcentos core]$ git diff --color views.py
diff --git a/django/core/views.py b/django/core/views.py
index ae76eb3..6e4d832 100644
--- a/django/core/views.py
+++ b/django/core/views.py
@@ -11,6 +11,7 @@ class MovieList(ListView):
     # It will query for all the rows of that model, pass it to the template
     # and returned the rendered template in a response.
     model = Movie
+    paginate_by = 2
 
 class MovieDetail(DetailView):
     model = Movie
(MyMDB) [kuvivek@vivekcentos core]$ 

```

Running the test once again.

(MyMDB) [kuvivek@vivekcentos django]$ 
(MyMDB) [kuvivek@vivekcentos django]$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.047s

OK
Destroying test database for alias 'default'...
(MyMDB) [kuvivek@vivekcentos django]$

This time it successfully passed.


24. Adding Person and model relationships.

In this section, we will add relationships between models to this project. People's relationship to movies can create a complex data model. The same person can be the actor, writer,
and director (for example, The Apostle (1997) written, directed, and starring Robert Duvall). Even leaving out the crew and production teams and simplifying a bit, the data model will 
involve a one-to-many relationship using a `ForeignKey` field, a many-to-many relationship using a `ManyToManyField`, and a class that adds extra information about a many-to-many 
relationship using a through class in a `ManyToManyField`.

   Lets create the following steps:
   1. Create a Person model.
   2. Add a `ForeignKey` field from `Movie` to `Person` to track the director.
   3. Add a `ManyToManyField` from `Movie` to `Person` to track the writers.
   4. Add a `ManyToManyField` with a through class(Actor) to track, who performed and in what role in a Movie.
   5. Create the migration.
   6. Add the director, writer, and actors to the movie details template.
   7. Add a `PersonalDetail` view to the list that indicates what movie a Person has directed, written, and performed in.

25. Adding a model with relationships.



