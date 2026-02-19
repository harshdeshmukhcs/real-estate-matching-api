from pydantic import BaseModel

class ListingCreate(BaseModel):
    price: int
    location: str
    bedrooms: int
    square_feet: int

class BuyerCreate(BaseModel):
    max_price: int
    preferred_location: str
    min_bedrooms: int
