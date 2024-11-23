FROM python:3.12.3-slim

WORKDIR /backend

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip --no-cache-dir &&  \
    pip install poetry --no-cache-dir &&  \
    poetry install

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY app/ app/

COPY alembic/ alembic/
COPY alembic.ini migrate.sh entrypoint.sh seed.sh ./

RUN chmod +x entrypoint.sh
