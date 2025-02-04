import unittest
from datetime import datetime
from src.parser import Parser
from src.models import Product

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(class_name="test-class")

    def test_parse_single(self):
        html = "<html><body><div class='test-class'>Test Content</div></body></html>"
        result = self.parser.parse_single(html, 'div')
        self.assertEqual(result, "Test Content")

    def test_parse_products(self):
        html = """
        <html>
            <body>
                <div class='test-class'>
                    <span class='product-name'>Test Product</span>
                    <span class='price-per-unit'>10.0</span>
                    <span class='price-per-kg'>20.0</span>
                    <span class='offer-price'>15.0</span>
                    <span class='clubcard-price'>12.0</span>
                    <span class='offer-dates'>01/01/2023</span>
                    <span class='clubcard-offer-dates'>02/01/2023</span>
                </div>
            </body>
        </html>
        """
        products = self.parser.parse_products(html)
        self.assertEqual(len(products), 1)
        product = products[0]
        self.assertEqual(product.Name, "Test Product")
        self.assertEqual(product.Price, 10.0)
        self.assertEqual(product.PricePerKg, 20.0)
        self.assertEqual(product.OfferPrice, 15.0)
        self.assertEqual(product.OfferPriceClubCard, 12.0)
        self.assertEqual(product.DateOfOffer, datetime(2023, 1, 1))
        self.assertEqual(product.DateOfOfferClubCard, datetime(2023, 1, 2))

if __name__ == '__main__':
    unittest.main()