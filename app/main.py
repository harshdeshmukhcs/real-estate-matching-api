from fastapi import FastAPI
from .database import engine, Base
from .routers import listings, buyers, analytics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Real Estate Lead Matching API")

Base.metadata.create_all(bind=engine)

app.include_router(listings.router)
app.include_router(buyers.router)
app.include_router(analytics.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Real Estate Matching Service Running"}
