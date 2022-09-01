# FastAPI and React Simple App with Azure Deployment Guide

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)

## Requirements 🏃

- Familiarity with FastAPI and Python
- Knowledge of React and Javascript
- Bit of knowledge about deployment and MS Azure

The idea to create this originated through a recent requirement of app deployment to Azure cloud in my current organization. I went through some tutorials and blogs, had 
a paid account activated on Azure to experiment with various features Azure has to offer.

This app started as a simple Fast-API app but now, it has a frontend integrated which is written in React. I also plan to test this with MS SQL Server and Postgres in the 
future.

## Features

- User authentication 📦
- CRUD on recipes module.
- Recipes can have multiple images 🍗
- Recipes can have multiple steps 🚶
- Recipes can have multiple ingredients 🔖


## Start Script for Azure

Put this under Settings --> Configuration --> General --> Startup Command

```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Deployment

Deployed on Azure currently on this url https://amit-fastapi.azurewebsites.net/
By the time you might be reading this the link might not be working anymore.

