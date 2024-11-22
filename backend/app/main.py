from fastapi import FastAPI

from .api import api_router
from .core.database import init_db


app = FastAPI(
    title="Insurance Service",
    description="API для расчёта стоимости страхования и управления тарифами",
    version="1.0.0",
)

app.include_router(api_router)


init_db()

# @app.on_event("startup")
# def on_startup():
#     init_db()
