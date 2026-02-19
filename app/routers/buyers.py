from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, services
from ..database import get_db

router = APIRouter()

@router.post("/buyers")
def create_buyer(
    buyer: schemas.BuyerCreate,
    db: Session = Depends(get_db)
):
    db_buyer = models.Buyer(**buyer.dict())
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer


@router.get("/match/{buyer_id}")
def match_buyer(
    buyer_id: int,
    db: Session = Depends(get_db)
):
    buyer = db.query(models.Buyer).filter(models.Buyer.id == buyer_id).first()

    if not buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")

    listings = db.query(models.Listing).all()
    matches = []

    for listing in listings:
        score = services.calculate_match_score(listing, buyer)
        if score > 0:
            matches.append({
                "listing_id": listing.id,
                "score": score
            })

    return {
        "matches": sorted(matches, key=lambda x: x["score"], reverse=True)
    }
