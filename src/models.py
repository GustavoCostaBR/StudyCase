from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    name: str
    price: float
    url: str
    timestamp: datetime = datetime.now()  # Auto-populate timestamp