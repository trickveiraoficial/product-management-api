from fastapi import FastAPI

app = FastAPI()

from .routes.product_routes import setup_routes

setup_routes(app)