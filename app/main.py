from fastapi import FastAPI
from .database import engine, Base
from .routers import listings, buyers, analytics

app = FastAPI(title="Real Estate Lead Matching API")

Base.metadata.create_all(bind=engine)

app.include_router(listings.router)
app.include_router(buyers.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Real Estate Matching Service Running"}
