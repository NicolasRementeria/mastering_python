***Flask Python Calculator***

___

1- Install Pipenv

- > pip3 install pipenv

2- Run virtual enviornment

- > pipenv shell

3- Install Flask

- > pipenv install flask

___

***File Setup***

- > from flask import Flask, render template, request

***VSCode - Linting and Formatter Issues***

*Make sure you are inside your virtual enviornment*

- > pipenv install pylint
- > pipenv install autopep8

**VSCode Helpful Extension**
- "Better TOML": To highlight Pipfile
___

***To test the App:***

- > flask run

Output Example:

```
$  flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
[2020-05-16 18:51:26,382] ERROR in app: Exception on / [GET]
```

___

Tutorial followed: 

- https://github.com/nanoproductions/flask_calculator_basic#flask-python-calculator
- https://www.youtube.com/watch?v=ia0rvIfxPFc