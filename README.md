# Foreign Exchange Trades
This is a application for search **cats** in a graph of stations and tubes, where the owners check all the stations, if is possible, trying to find their cats.
This is a web app to convert one currency into another.

# Run Application

To run the application you should have python3 and virtualenv installed 

```
brew install python3
```
```
pip install virtualenv
```

If you don't have brew installed you can check [a here link](https://brew.sh/)

With python3 you already have pip installed

Go to the root of the project (cd myproject) and just run the following commands:

```
virtualenv venv
source venv/bin/activate
```
Now you can see, (venv) in the console, we are on the virtualenv lets go and install all the requirements

```
pip install -r requirements.txt
```

Now we have all the requirements installed

We have 2 ways to run this app locally or with docker

#Locally

For the first one, you need to install postgresql 

```
brew install postgresql
```

You should now be in a shell session for the postgres user. Log into a Postgres session by typing:

```
psql
```

First, we will create a database for our Django project.

```
CREATE DATABASE myproject;
```

Next, we will create a database user which we will use to connect to and interact with the database. Set the password to something strong and secure:

```
CREATE USER myprojectuser WITH PASSWORD 'password';
```

We are setting the default encoding to UTF-8, we are also setting the default transaction isolation scheme to "read committed", which blocks reads from uncommitted transactions. Lastly, we are setting the timezone to UTC.

```
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

Now, all we need to do is give our database user access rights to the database we created:

```
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

Exit the SQL prompt to get back to the postgres user's shell session:

```
\q
```

Now, update the settings django file (foreign_exchange_trades/setting.py) and update the part of DATABASES with your current user, dbname and password. Make sure that HOST is localhost.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'mypassword'
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

We are set, just run django:

```
python manage.py runserver
```

# Docker
For the second, run the webapp into docker just run:

```
docker-compose build
docker-compose up -d db
docker-compose up -d
```

With the first line we build the docker image, first we lunch the database service (db), to avoid some connection errors, then lunch all the services, we have 3 services, db (database), web (our django webapp) and nginx (server)

And we are set! You can go to http://0.0.0.0:8000 or localhost:8000

To stop the docker containers, just run:

```
docker-compose stop
```

If you want to restart:
```
docker-compose up -d
```

Also if the cointainers are stopped, you can remove them with:

```
docker-compose rm
```

if you want to see the command line of the docker run:

```
docker-compose up
```

With the flag -d we just say run like daemon

# Tests

We are going to use **selenium** and **Firefox**

To run the tests, you should have firefox installed and run:

```
cp drivers/geckodriver venv/bin/
python tests/trade_app_test.py
```

The first line is copy a driver which is used by selenium and python
This is going to open a new windows on firefox and test the app

Also, we have some tests for check some backend functions, you can run them with this command:

```
python manage.py test
```

This last test only can run locally, with docker throws some errors.
