from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def dashboard(request: Request):
    """
    Displays information about stocks in the system
    """
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.post("/stock")
def create_stock():
    """Creates a stock and saves it in the database"""
    return {"code": "success", "message": "Stock added"}
