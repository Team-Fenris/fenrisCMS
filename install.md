
# Prerequisites
* Works on both Windows and Linux (preferably either Debian or Debian-based distribution)
* Minimum 2GB RAM
* Minimum 16GB HDD

# Installation

### Quick install

1. Open powershell and navigate to a folder you like the code to be stored.
2. Run command ``git clone https://github.com/Team-Fenris/fenrisCMS.git``
3. Run command ``pip install -r requirements.txt``
4. Open folder in a IDE(preferably)
5. Create a database
6. Edit database settings in Settings.py
7. Run ``python manage.py makemigrations``
8. Run ``python manage.py migrate``
### Manuel Windows Python/Git

1. Open powershell as ``admin``.
```
start-process powershell -verb ruans
```
Or you can search "Powershell", rightclick and ``Run as administrator``.

2. Use the ``cd`` command to navigate to a directory you want to work in.
 Once inside the directory of your choice run ``mkdir`` command and give your new directory a name.
 
3. If you want to use a virtual enviorment you can install pyenv inside the newly created directory. Inside powershell run the command ``pip install virualenv`` to install and to run ``virtualenv pyenv``. whenever you want to work inside the ``virtualenv pyenv`` you run ``.\pyenv\scripts\activate`` inside powershell.

4. In powershell type ``Python`` and check if it is installed.
if it isn`t installed run ``pip install python``.
5. Install ``django-datatables-view``, in Powershell type ``pip install django-datatables-view``

5. To interact with the database using Python we also need to install a database interpreter, in Powershell run ``pip install psycopg2``. This is a Python specific PostgreSQL adapter for issuing commands to  the database.
6. We are also going to need Git in order to clone the repo. Depending if your  using an IDE like Visual studio code or your using powershell. If you're using VScode you import the Git module. If you're using windows and powershell follow this guide ``https://www.develves.net/blogs/asd/articles/using-git-with-powershell-on-windows-10/``
7. After installing all the different applications and dependecies we are finally going to clone the Repo. Navigate to the folder where you created the virtual enviorment and type ``git clone https://github.com/Team-Fenris/fenrisCMS.git``.
8. 
### Postgresql install
1. We are using PostgreSQL so you need to install that aswell. Its very simple, go to ``https://www.postgresqltutorial.com/install-postgresql/`` and follow their guide.
2. Once completed with the postgres installation open up ``SQL Shell (psql)`` and login to your database and we're going to create a new user.
3. Create a new user to work with from django.

```
CREATE USER username WITH PASSWORD 'password';
```
Next we will give access to the database for the new database and user we created.
```
GRANT ALL PRIVILEGES ON DATABASE database TO username;
```
Now that we are done type
```
\q
```
And exit out of the postgres shell
```
exit
```
4. After the user has been created and access to the user have been given we have to change some settings in the settings.py file.
5. Once the settings have been changed you run these two commands in the main directory 
```python manage.py makemigrations```
```python manage.py migrate```


### Linux installation
When installing Linux (e.g. Ubuntu), create a user called `testdev`.

1. Install packages needed.

`sudo apt install python3-pip python3-psycopg2 git`

2. Install packages

`sudo apt-get update && apt-get install apache2 git python3 postgresql postgresql-contrib postgresql libpq-dev postgresql-client python3-dev libpq-dev curl ca-certificates python3-pip -y`

3. Edit `pg_hba.conf`
Change from this line:

`local   all             postgres                                peer`

to

`local   all             postgres,testdev                                peer`

4. Start PostgreSQL
`sudo systemctl start postgresql`

4.1 We are using PostgreSQL so you need to install that aswell. Its very simple, go to ``https://www.postgresqltutorial.com/install-postgresql/`` and follow their guide.

4.2 Once completed with the postgres installation open up `psql` and login to your database and we're going to create a new user.

4.3 Create a new user to work with from django

```
CREATE DATABASE fenrisdb;

CREATE USER testdev WITH PASSWORD 'testdev';
```

Next we will give access to the database for the new database and user we created.

```
GRANT ALL PRIVILEGES ON DATABASE fenrisdb TO testdev;
```
Now that we are done type
```
\q
```
And exit out of the postgres shell
```
exit
```

You should be able to run the following command from the `testdev` user when logged into the Linux terminal:

`psql -d fenrisdb -U testdev`

When this is up and running, and works, Django can be integrated.

6. Clone the repository

`git clone https://github.com/Team-Fenris/fenrisCMS.git`

7. Install Python libraries

`cd fenrisCMS`

`pip3 install -r requirements.txt`

8. Change settings.py

```
ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", "your-ip-address-here"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fenrisdb',
        'USER': 'testdev',
        'PASSWORD': 'testdev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

9. Run migrations to install the Django data to the database

```
$ cd fenrisCMS
testdev@testdev:~/fenrisCMS $ python3 manage.py makemigrations
testdev@testdev:~/fenrisCMS $ python3 manage.py migrate
```

On the prompt if any fields are changed, choose *no* on all.

10. Run the Django server

```
testdev@testdev:~/fenrisCMS $ python3 manage.py runserver 0.0.0.0:8000
```

Your Django server should now be up and running, and you should get a message like:

```
System check identified 8 issues (0 silenced).
April 11, 2021 - 16:44:05
Django version 3.2, using settings 'loganalyzer.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

You can now request Django on https://<Django-IP>:8000
