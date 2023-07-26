import logging

from fastapi import FastAPI
from routes import routers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

app = FastAPI()

app.include_router(routers)
