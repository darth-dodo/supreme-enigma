# Fun with FastAPI

## Table of contents:
- [Setup and Install](#setup-and-install)
- [Hello World demo](#hello-work-demo)

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