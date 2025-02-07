import unittest
from src.fetcher import Fetcher
from src.parser import Parser
from src.models import Product

class TestIntegration(unittest.TestCase):
    def test_fetch_and_parse(self):
        fetcher = Fetcher("https://nakup.itesco.cz/groceries/en-GB/search?query=milk", "product-details--wrapper")
        html = fetcher.fetch_html()

        parser = Parser(class_name="product-details--wrapper")
        products = parser.parse_products(html)

        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)
        self.assertIsInstance(products[0], dict)
        self.assertIn("Name", products[0])
        self.assertIn("Price", products[0])
        self.assertIn("PricePerKg", products[0])
        self.assertIn("OfferPrice", products[0])
        self.assertIn("OfferPriceClubCard", products[0])
        self.assertIn("DateOfOffer", products[0])
        self.assertIn("DateOfOfferClubCard", products[0])
        self.assertIn("Url", products[0])
        self.assertIn("Timestamp", products[0])

if __name__ == '__main__':
    unittest.main()