import json
import requests
from src.config import PRICE_SCRAPER_API_ENDPOINT_CREATE

class APICaller:
    """
    A caller class that sends product data to the API.
    """

    @classmethod
    def send_products(cls, products: list) -> None:
        """
        Serialize the list of product models to JSON and send it via POST request to the API endpoint.

        Args:
            products (list): A list of product objects from models.py.
                             Each product is expected to have a `to_json()` method for serialization.
        """
        # Convert each product to a JSON string using the to_json method
        data = [product.to_json() for product in products]

        # Print the data being sent to the API
        print("Data being sent to API:", data)

        try:
            response = requests.post(PRICE_SCRAPER_API_ENDPOINT_CREATE, json=json.dumps(data))
            if response.ok:
                print("POST successful:", response.status_code)
            else:
                print("POST failed:", response.status_code, response.text)
        except Exception as e:
            print("An error occurred while calling the API:", e)