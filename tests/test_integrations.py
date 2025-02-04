import unittest
from src.fetcher import Fetcher
from src.parser import Parser
from src.models import Product

class TestIntegration(unittest.TestCase):
    def test_fetch_and_parse(self):
        fetcher = Fetcher("http://example.com", "test-class")
        html = fetcher.fetch_html()

        parser = Parser(class_name="test-class")
        products = parser.parse_products(html)

        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)
        self.assertIsInstance(products[0], Product)

if __name__ == '__main__':
    unittest.main()