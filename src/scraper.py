from typing import Optional
from bs4 import BeautifulSoup
import requests
from .models import Product
from .config import BASE_URL  # Assume config.py defines this

class PriceScraper:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def fetch_html(self, url: str) -> Optional[str]:
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_product(self, html: str) -> Optional[Product]:
        soup = BeautifulSoup(html, "html.parser")
        # Example: Replace with your target site's selectors
        name = soup.find("h1").get_text(strip=True)
        price_str = soup.select_one(".price").get_text(strip=True)
        price = float(price_str.replace("$", "").replace(",", ""))

        return Product(
            name=name,
            price=price,
            url=self.base_url
        )