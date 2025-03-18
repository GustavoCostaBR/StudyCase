import requests
from src.config import PRICE_SCRAPER_API_ENDPOINT_CREATE_PRODUCTS

class APICaller:
    """
    A caller class that sends product data to the API.
    """

    @classmethod
    def send_products(cls, products: list) -> None:
 
        data = [product.to_dictionary() for product in products]

        try:
            response = requests.post(PRICE_SCRAPER_API_ENDPOINT_CREATE_PRODUCTS, json=data)
            if response.ok:
                print("POST successful:", response.status_code)
            else:
                print("POST failed:", response.status_code, response.text)
        except Exception as e:
            print("An error occurred while calling the API:", e)