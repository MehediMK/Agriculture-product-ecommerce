<h1 align='center'>Agriculture product ecommerce</h1>


## Prerequisites
  - Python 3.8+
  - Virtualenv and Pip

## How to Run this Project

  - Clone this Project
  - `cd <project_directory>` 
  - create `virtualenv env`
  - For activate env `source env/bin/activate` (*linux) on `env\Scripts\activate` (Windows)
  - Install packages `pip install -r requirements.txt`
  - `copy "config.py.sample" config.py`
  - Open any editor/ `nano config.py` (*linux) past you config
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py runserver`

## Helpful commands
  - `python manage.py makemigrations` "for migration"
  - `python manage.py makemigrations <app_name>` "for migration"
  - `python manage.py runserver host:port` "for starting dev. server"
  - `python manage.py startapp app_name` "for new app"
  - `python manage.py createsuperuser` "For create superuser"
