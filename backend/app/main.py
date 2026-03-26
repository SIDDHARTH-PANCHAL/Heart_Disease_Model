from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Heart Disease Prediction API")

app.include_router(router)