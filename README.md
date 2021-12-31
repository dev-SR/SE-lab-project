# Software Engineering Lab Project Using Django

- [Software Engineering Lab Project Using Django](#software-engineering-lab-project-using-django)
	- [Introduction](#introduction)
	- [Deployment](#deployment)
		- [Add Environment Variables](#add-environment-variables)
		- [Configuring the DataBase](#configuring-the-database)
		- [Static files](#static-files)

## Introduction

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
```
