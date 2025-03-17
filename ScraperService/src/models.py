from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    Name: str
    Price: float
    PricePerKg: Optional[float] = None
    OfferPrice: Optional[float] = None
    OfferPriceClubCard: Optional[float] = None
    Url: str
    DateOfOffer: Optional[datetime] = None
    DateOfOfferClubCard: Optional[datetime] = None

    def to_dictionary(self) -> dict:
        """
        Serialize the Product instance to a dictionary.
        """
        data = self.model_dump(exclude_none=True)
        # Convert datetime objects to ISO format strings
        if 'DateOfOffer' in data and data['DateOfOffer']: 
            data['DateOfOffer'] = data['DateOfOffer'].isoformat()
        if 'DateOfOfferClubCard' in data and data['DateOfOfferClubCard']:
            data['DateOfOfferClubCard'] = data['DateOfOfferClubCard'].isoformat()

        return data