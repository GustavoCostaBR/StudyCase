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

    def to_json(self) -> str:
        """
        Serialize the Product instance to a JSON string containing only its fields.
        """
        return self.model_dump_json()  # Only the model fields are included by default
        