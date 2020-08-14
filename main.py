from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Stock
import yfinance as yf

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
def dashboard(
    request: Request,
    forward_pe=None,
    dividend_yield=None,
    ma50=None,
    ma200=None,
    db: Session = Depends(get_db),
):
    """
    Displays information about stocks in the system
    """

    stocks = db.query(Stock)

    if forward_pe:
        stocks = stocks.filter(Stock.forward_pe < forward_pe)

    if dividend_yield:
        stocks = stocks.filter(Stock.dividend_yield > dividend_yield)

    if ma50:
        stocks = stocks.filter(Stock.price < Stock.ma50)

    if ma200:
        stocks = stocks.filter(Stock.price < Stock.ma200)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "stocks": stocks,
            "forward_pe": forward_pe,
            "dividend_yield": dividend_yield,
            "ma50": ma50,
            "ma200": ma200,
        },
    )


def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()

    yahoo_data = yf.Ticker(stock.symbol)
    result = yahoo_data.info

    stock.ma200 = result["twoHundredDayAverage"]
    stock.ma50 = result["fiftyDayAverage"]
    stock.price = result["previousClose"]
    stock.forward_pe = result["forwardPE"]
    stock.forward_eps = result["forwardEps"]

    if result["dividendYield"]:
        stock.dividend_yield = result["dividendYield"] * 100

    db.add(stock)
    db.commit()


@app.post("/stock")
async def create_stock(
    stock_request: StockRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """Creates a stock and saves it in the database"""

    stock = Stock()
    stock.symbol = stock_request.symbol

    db.add(stock)
    db.commit()

    background_tasks.add_task(fetch_stock_data, stock.id)

    return {
        "code": "success",
        "message": "Stock added",
        "stock_id": stock.id,
        "stock_symbol": stock.symbol,
    }
