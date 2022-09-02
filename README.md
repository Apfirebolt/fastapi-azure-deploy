# FastAPI and React Simple App with Azure Deployment Guide

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)

## Requirements 🏃

- Familiarity with FastAPI and Python
- Knowledge of React and Javascript
- Bit of knowledge about deployment and MS Azure

The idea to create this originated through a recent requirement of app deployment to Azure cloud in my current organization. I went through some tutorials and blogs, had a paid account activated on Azure to experiment with various features Azure has to offer.

This app started as a simple Fast-API app but now, it has a frontend integrated which is written in React. I also plan to test this with MS SQL Server and Postgres in the 
future.

## Issues

- I was not able to execute multiple startup commands once the app is deployed, I manually had to run migrations which I wanted to be automated.
- Don't know how to access the app directory and the venv to execute commands through SSH.

## Start Script for Azure

Put this under Settings --> Configuration --> General --> Startup Command

```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Deployment

Setup the application variables to set the connection with Azure Postgres instance. **Configuration** --> **App Settings**.

For Postgres add the IP address of the server which would be hosting the FastAPI App. **Connection Security** --> **Firewall Rule Name**.

Also, check access to Azure apps toggle button.

```
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
```

React frontend build is generated on the development machine and it is directed through jinja templates.

Deployed on Azure currently on this url https://amit-fastapi.azurewebsites.net/
By the time you might be reading this the link might not be working anymore.

