FROM python:3.13-slim

WORKDIR /backend

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip --no-cache-dir &&  \
    pip install poetry --no-cache-dir &&  \
    poetry install

COPY app/ app/

COPY entrypoint.sh ./

RUN chmod +x entrypoint.sh
