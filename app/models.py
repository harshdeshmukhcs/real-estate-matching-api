from sqlalchemy import Column, Integer, String
from .database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    location = Column(String)
    bedrooms = Column(Integer)
    square_feet = Column(Integer)

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    max_price = Column(Integer)
    preferred_location = Column(String)
    min_bedrooms = Column(Integer)
