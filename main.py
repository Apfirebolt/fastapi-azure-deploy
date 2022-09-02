from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from todo import todo_router
from account import router as account_router

import db

app = FastAPI()

app.mount("/static", StaticFiles(directory="client/build/static"), name="static")

templates = Jinja2Templates(directory="client/build")

@app.on_event("startup")
async def startup():
    print('Started now, db')


@app.on_event("shutdown")
async def shutdown():
    print('ended now db')

@app.get("/home")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
async def welcome():
    return {
        "message": "Hello World Sample API"
    }

app.include_router(todo_router)
app.include_router(account_router.router)