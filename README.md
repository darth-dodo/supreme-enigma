# Fun with FastAPI

## Table of contents:
- [Setup and Install](#setup-and-install)
- [Hello World demo](#hello-work-demo)
- [Stocks Dashboard](#stocks-dashboard)
    - [Database Design](#database-design)

## Setup and Install
- Install Pyenv and set the local python version to 3.8.3
- Install Poetry
- Clone the repo
- Run `poetry install`
- Get inside the virtual environment using `poetry shell`

## Hello World Demo

- Run the server using the command `uvicorn main:app --reload` or my fancy `make` command `make server`
- Go to http://localhost:8000/
- Go to http://localhost:8000/items/12
- Go to http://localhost:8000/items/12?query=apples%20are%20yummy


## Stocks Dashboard
- Head to http:localhost:8000/docs for API documentation
- Head to http:localhost:8000 for list of all the stocks

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