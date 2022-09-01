from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from todo import todo_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="client/build/static"), name="static")

templates = Jinja2Templates(directory="client/build")

@app.get("/home")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
async def welcome():
    return {
        "message": "Hello World Sample API"
    }

app.include_router(todo_router)