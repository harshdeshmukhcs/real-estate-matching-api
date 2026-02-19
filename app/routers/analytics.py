from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models
from ..database import get_db

router = APIRouter()

@router.get("/analytics/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):
    total_listings = db.query(models.Listing).count()
    total_buyers = db.query(models.Buyer).count()
    avg_price = db.query(func.avg(models.Listing.price)).scalar()

    return {
        "total_listings": total_listings,
        "total_buyers": total_buyers,
        "average_listing_price": avg_price
    }
