from fastapi import FastAPI
from app.routers import calcampi

app = FastAPI(
    title="Calcampi API",
    description="API para cálculo de propiedades de péptidos",
    version="1.0.0"
)

app.include_router(calcampi.router, prefix="/calcampi", tags=["Calcampi"])

#uvicorn app.main:app --reload

