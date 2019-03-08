# Restaurant App - FrauenLoop

Building a web app using Python, Flask.

## SETUP

I assume you already installed Python 3.4 or higher and pip.

### Virtual Environment

Install virtualenv via pip:

```
$ pip3 install virtualenv
```

Create a virtual environment for a project:

```
$ cd restaurant-app
$ python3 -m venv myvenv
```

To begin using the virtual environment, it needs to be activated:

```
$ source myvenv/bin/activate
```

Install Flask:

```
(venv) $ pip3 install flask
```

### Run server

With this command:

```
(venv) $ export FLASK_APP=run.py
(venv) $ export PYTHONPATH=/Path/to/the/app
(venv) $ flask run
```

### In Browser

Paste this url and hit enter:

```
http://localhost:5000/restaurants
```

### Tests

You can run the tests with this command:

```
(venv) $ python3 project/test_views.py
```

### API Architecture

- **GET restaurants/** – Retrieves list of restaurants
- **GET restaurant/<public_id>** – Retrieves the one restaurant details of the <public_id>
- **POST restaurant/** – Create a new restaurant without authentication
- **DELETE user/<public_id>** – Delete the restaurant of the <public_id>
- **PATCH restaurants/<public_id>** – Update the restaurant of the <public_id>

### What is not working?
(only example!)

- integration tests are not running properly:
	1. `test_create_user_works_unauthenticated` should work and return the POST method should return the response code 201.
	2. `test_create_user_fails_authenticated` is not able to login, this does not work because of the request context in Flask (<http://flask.pocoo.org/docs/0.12/reqcontext/>).

### Suggestions for Improvement
(only example!)

- it would be great to have **migrations** for changes that happen in the database fields/tables - possible to do with Alembic that is installed with requirements.txt.
- **more integration tests** in `test_views.py` are needed for checking RESTful architechture: very important for catching errors that could return the response code 500, overwriting wrong success response codes and giving appropriate error messages if the HTTP request is not successful
- **unit tests** for the `models.py` and `forms.py` are missing
