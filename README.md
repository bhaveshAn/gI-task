# Give India - Backend Developer Challenge

[Heroku Link](https://fathomless-spire-13788.herokuapp.com)

API endpoints

All endpoints are [here](/app/api/__init__.py) and must have header as build on Flask REST JsonAPI with JSON 1.0 Specification

`Content-Type: "application/vnd.api+json"`

1. * GET & POST * [/process/](https://fathomless-spire-13788.herokuapp.com/process/) 
2. * GET & DELETE * [/process/<int:id>](https://fathomless-spire-13788.herokuapp.com/process/1) 
3. * GET & DELETE * [/process/<int:id>](https://fathomless-spire-13788.herokuapp.com/process/1)
4. * GET* [/stats](https://fathomless-spire-13788.herokuapp.com/stats) 

## Installation

1. Install Python 3

```
sudo apt-get install python3
```

2. Install PostgreSQL

```
sudo apt-get install postgresql postgresql-contrib
```

3. Install Dependendies (via virtual environment)

```
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

```

4. Creating Postgres Database

```
sudo -u postgres psql

```

> Inside Postgres Shell

```
CREATE USER john WITH PASSWORD 'start';
CREATE DATABASE gindia WITH OWNER john;
```

## Running the App (Steps)

```
cp .env.example .env

python3 create_db.py

python3 manage.py runserver

```

> For Upgrading the Database

```
python3 manage.py db upgrade
```

> For Downgrading the Database

```
python3 manage.py db downgrade
```

> For Migrating the Database

```
python3 manage.py db migrate
```
