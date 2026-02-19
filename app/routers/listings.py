from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/listings")
def create_listing(
    listing: schemas.ListingCreate,
    db: Session = Depends(get_db)
):
    db_listing = models.Listing(**listing.dict())
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing


@router.get("/listings")
def get_listings(
    db: Session = Depends(get_db)
):
    return db.query(models.Listing).all()
