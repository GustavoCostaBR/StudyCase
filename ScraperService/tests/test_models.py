import unittest
from datetime import datetime
from src.models import Product

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product(
            Name="Test Product",
            Price=10.0,
            PricePerKg=20.0,
            OfferPrice=15.0,
            OfferPriceClubCard=12.0,
            Url="http://example.com",
            DateOfOffer=datetime(2023, 1, 1),
            DateOfOfferClubCard=datetime(2023, 1, 2),
            Timestamp=datetime(2023, 1, 3)
        )
        self.assertEqual(product.Name, "Test Product")
        self.assertEqual(product.Price, 10.0)
        self.assertEqual(product.PricePerKg, 20.0)
        self.assertEqual(product.OfferPrice, 15.0)
        self.assertEqual(product.OfferPriceClubCard, 12.0)
        self.assertEqual(product.Url, "http://example.com")
        self.assertEqual(product.DateOfOffer, datetime(2023, 1, 1))
        self.assertEqual(product.DateOfOfferClubCard, datetime(2023, 1, 2))
        self.assertEqual(product.Timestamp, datetime(2023, 1, 3))

if __name__ == '__main__':
    unittest.main()