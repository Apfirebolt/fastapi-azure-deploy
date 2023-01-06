from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from account import router as account_router

import db

app = FastAPI()

app.mount("/static", StaticFiles(directory="client/build/static"), name="static")

templates = Jinja2Templates(directory="client/build")

@app.get("/about")
async def not_timed():
    return {"message": "Added about message - January 2022"}

@app.get("/{full_path:path}")
async def serve_react_app(request: Request, full_path: str):
    """Serve the react app
    `full_path` variable is necessary to serve each possible endpoint with
    `index.html` file in order to be compatible with `react-router-dom
    """
    return templates.TemplateResponse("index.html", {"request": request})
    

app.include_router(account_router.router)