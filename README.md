# (주)Kinpecauto tacar RESTful API

Article information management and article location information are tracked.

## Technology
* Python 3.6
* Django 3.0.6
* Django Rest Framework 3.11.0
* psycopg2 2.8.5
* django-cors-headers 3.2.1
* bcrypt 3.1.7
* pillow 7.1.2
* boto3 1.13.23
* pyfcm 1.4.7

### Prerequisites

What things you need to install the software and how to install them

```
python --version (3.6.8)
```

### Installing

A step by step series of examples that tell you how to get a development env running

RESTful Web Services

```
pip install djangorestframework
```

Management setuptools

```
pip install -U setuptools
```

Connect Django project to PostgreSQL Option

```
pip install psycopg2-binary
```

Connect Django project to PostgreSQL

```
pip install psycopg2
```

Configure CORS

```
pip install django-cors-headers
```

Password Encryption

```
pip install bcrypt
```

JWT(Json Web Tokens)

```
pip install pyjwt
```

AWS SDK(Boto3)

```
pip install boto3
```

Python image library

```
pip install pillow
```

FCM – send push notifications using Python

```
pip install pyfcm
```

Date range filter

```
pip install django-admin-rangefilter
```

openpyxl is a Python library to read/write xlsx/xlsm/xltx/xltm files.

```
pip install openpyxl
```

Http Request handling

```
pip install requests
```

Date range filter

```
pip install django-admin-rangefilter
```

Mysql Database Connection

```
pip install mysqlclient
```

openpyxl is a Python library to read/write xlsx/xlsm/xltx/xltm files.

```
pip install openpyxl
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

```
python manage.py runserver 0.0.0.0:7000
nohup python manage.py runserver 0.0.0.0:7000 1> /dev/null 2>&1 &
```

### Requirements Info
```
pip freeze > requirements.txt

pip install -r requirements.txt
```

## Authors

* **mgkwon** - *Initial work* - (주)킨펙오토

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Good luck