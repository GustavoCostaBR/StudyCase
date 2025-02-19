import unittest
from datetime import datetime
from src.parser import Parser
from src.models import Product
from src import config as cfg

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser(class_name="test-class")

    def test_parse_single(self):
        html = "<html><body><div class='test-class'>Test Content</div></body></html>"
        result = self.parser.parse_single(html, 'div')
        self.assertEqual(result, "Test Content")

    def test_parse_products(self):
        html = f"""
        <html>
            <body>
                <div class='test-class'>
                    <span class='{cfg.SPAN_PRODUCT_NAME_CLASS}'>Test Product</span>
                    <span class='{cfg.P_PRICE_PER_UNIT_CLASS}'>70,13 Kč</span>
                    <span class='{cfg.P_PRICE_PER_KG_CLASS}'>99,90 Kč/kg</span>
                    <span class='{cfg.SPAN_OFFER_PRICE_CLASS}'>-41%, předtím 84,90 Kč, teď 49,90 Kč</span>
                    <span class='{cfg.P_CLUBCARD_PRICE_CLASS}'>S Clubcard 79.99 Kč, běžná cena 99.90 Kč</span>
                    <span class='{cfg.SPAN_OFFER_DATES_CLASS}'>Offer valid until 04/02/2025</span>
                    <span class='{cfg.SPAN_CLUBCARD_OFFER_DATES_CLASS}'>Offer valid until 04/02/2025</span>
                </div>
            </body>
        </html>
        """
        products = self.parser.parse_products(html)
        print(products)
        self.assertEqual(len(products), 1)
        product = products[0]
        self.assertEqual(product['Name'], "Test Product")
        self.assertEqual(product['Price'], 70.13)
        self.assertEqual(product['PricePerKg'], 99.9)
        self.assertEqual(product['OfferPrice'], 49.9)
        self.assertEqual(product['OfferPriceClubCard'], 79.99)
        self.assertEqual(product['DateOfOffer'], datetime(2025, 2, 4))
        self.assertEqual(product['DateOfOfferClubCard'], datetime(2025, 2, 4))

if __name__ == '__main__':
    unittest.main()