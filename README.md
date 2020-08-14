# Fun with FastAPI

- FastAPI is the "new kid on the block" with regards to Python frameworks
- It is based on Starlette and brings several more cool features
- This demo is a rapid prototype created using Yahoo Finance APIs and fullstack FastAPI with Jinja2 templating engine
- The application can take in multiple stock symbols through the UI and fetch the financial data asynchronously using FastAPI Background Tasks
- The listing page offers basic query params based filtering
- The screenshots can be found [over here](#application-screenshots)

## Table of contents:
- [Application Screenshots](#application-screenshots)
- [Setup and Install](#setup-and-install)
- [Hello World demo](#hello-work-demo)
- [Yahoo Finance](#yahoo-finance)
- [Stocks Dashboard](#stocks-dashboard)
    - [Database Design](#database-design)

## Application Screenshots
- Adding multiple stocks ![Adding multiple stocks](/screenshots/01_adding_multiple_stocks.png?raw=true "Adding multiple stocks")
- Async data update using Background Tasks ![Async data update using Background Tasks](/screenshots/02_async_data_fetch.png?raw=true "Async data update using Background Tasks")
- Data persistance and Template Rendering ![Data persistance and Template Rendering](/screenshots/03_data_persistence_and_templating.png?raw=true "Data persistance and Template Rendering")
- Filtering based on query params ![Filtering based on query params](/screenshots/04_query_params_based_filtering.png?raw=true "Filtering based on query params")


## Setup and Install
- Install Pyenv and set the local python version to 3.8.3
- Install Poetry
- Clone the repo
- Run `poetry install`
- Get inside the virtual environment using `poetry shell`

## Hello World Demo

- Run the server using the command `uvicorn hello_world:app --reload` or my fancy `make` command `make helloworld`
- Go to http://localhost:8000/
- Go to http://localhost:8000/items/12
- Go to http://localhost:8000/items/12?query=apples%20are%20yummy

## Yahoo Finance
- The financial data is extracted using the Yahoo Finance library
- A demo of the library is present in the file `yfinance_demo.py` where a sample response is documented as well

## Stocks Dashboard
- Head to http://localhost:8000/docs for API documentation
- Head to http://localhost:8000 for list of all the stocks

### Database Design
- Database is created using SQLite and SQLAlchemy as the ORM
- The database structure is as follows:
```
(supreme-enignma-rOVS3nom-py3.8) ➜  supreme-enigma git:(feature/database-design) ✗ sqlite3 stocks.db
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE stocks (
        id INTEGER NOT NULL, 
        symbol VARCHAR, 
        price NUMERIC(10, 2), 
        forward_pe NUMERIC(10, 2), 
        forward_eps NUMERIC(10, 2), 
        dividend_yield NUMERIC(10, 2), 
        ma50 NUMERIC(10, 2), 
        ma200 NUMERIC(10, 2), 
        PRIMARY KEY (id)
);
CREATE UNIQUE INDEX ix_stocks_symbol ON stocks (symbol);
CREATE INDEX ix_stocks_id ON stocks (id);
sqlite> 
```


### Creating Stocks
- Pydantic to create `struct` or `POJO` equivalent for the incoming `POST` requests
- Dependency Injection used to make sure we have database connection while we are making a request
- Background Tasks for fetching the data from `yfinance` library

#### Pydantic
- Helps you structure your requests
- Handles controller level datatype validation
- Returns `422` response status code and descriptive payload in case of errors eg.
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "symbol"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```


#### Dependency Injection
- *Executing something depends on executing something else*
- Creating a stock depends on getting a database connection from the application
- This way we can use the `db` inside the controller layer
- `Depends` always have to come in the end of the function signature


#### Background Tasks
- Background tasks require the controller to be in the async mode
- The API is similar to Celery
- Inside the task, we are creating a new database session object and making persistent changes based on that
