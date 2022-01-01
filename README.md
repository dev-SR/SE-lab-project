# Software Engineering Lab Project Using Django

- [Software Engineering Lab Project Using Django](#software-engineering-lab-project-using-django)
  - [Introduction](#introduction)
  - [Custom Admin User](#custom-admin-user)
  - [Deployment](#deployment)
    - [Add Environment Variables](#add-environment-variables)
    - [Configuring the DataBase](#configuring-the-database)
    - [Static files](#static-files)

## Introduction


## Custom Admin User

Create new app with `python manage.py startapp users`

Add the following lines in the `settings.py` file:

```python
INSTALLED_APPS = [
    'users',
     #...
]
AUTH_USER_MODEL = 'users.User'
```

`users/models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
```

Stop Server and Delete `db.sqlite3` file.
Once deleted run `python manage.py makemigrations` and `python manage.py migrate` and create superuser with
`python manage.py createsuperuser`

Adding custom admin fieldset:


```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + \
        (("Custom Profile",
          {
              "fields":
              ("avatar",
               "gender",
               "bio",
               "birthdate",
               "language",
               "currency",
               "superhost",
               )
          },  # commas are must needed for tuple
          ),
         )
```


## Deployment

### Add Environment Variables

### Configuring the DataBase


### Static files


```bash
heroku login
heroku apps:create se-lab-pro
git remote -v
heroku plugins:install heroku-config
heroku config:push
heroku config:set DEBUG=True
heroku config:set DISABLE_COLLECTSTATIC=1

heroku run python manage.py migrate
heroku run python manage.py createsuperuser

```
