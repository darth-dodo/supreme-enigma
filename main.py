from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    """
    Displays information about stocks in the system
    """
    return {"Dashboard": "Homepage"}


@app.post("/stock")
def create_stock():
    """Creates a stock and saves it in the database"""
    return {"code": "success", "message": "Stock added"}
