FROM python:3.8.3-slim

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

ENV POETRY_VERSION=1.0.9
ENV POETRY_NO_INTERACTION=1

# Upgrade pip and install poetry
RUN pip install --upgrade pip && pip --no-cache-dir install poetry

# Create folder which will be the working directory
RUN mkdir /app

# Set /app as working directory
WORKDIR /app

# Copy the whole project into /app
COPY . .

# Avoid to create a new virtual environment (we are already in a docker image)
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install