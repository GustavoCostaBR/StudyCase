from pydantic import BaseModel
from datetime import datetime



class Product(BaseModel):
    Name: str
    Price: float
    PricePerKg: float
    OfferPrice: float
    OfferPriceClubCard: float
    Url: str
    DateOfOffer: datetime
    DateOfOfferClubCard: datetime
    Timestamp: datetime = datetime.now()  # Auto-populate timestamp