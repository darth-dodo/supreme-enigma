from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Stock

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def dashboard(request: Request):
    """
    Displays information about stocks in the system
    """
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.post("/stock")
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):
    """Creates a stock and saves it in the database"""

    stock = Stock()
    stock.symbol = stock_request.symbol

    db.add(stock)
    db.commit()

    return {"code": "success", "message": "Stock added"}
