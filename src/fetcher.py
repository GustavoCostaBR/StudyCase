from typing import Optional
from bs4 import BeautifulSoup, Tag  # Import Tag type
from bs4.element import ResultSet
import requests
from .models import Product
from .config import BASE_URL
from .config import HEADERS

class Parser:
	def __init__(self, base_url: str = BASE_URL):
		self.base_url = base_url
		self.session = requests.Session()
		self.session.headers = {
			**HEADERS,
			"Accept-Language": "en-US,en;q=0.9",
		}

	def fetch_html(self) -> Optional[str]:
		try:
			response = self.session.get(self.base_url, timeout=10)
			response.raise_for_status()
			if response.status_code != 200:
				print(f"Error fetching {self.base_url}: {response.status_code} - {response.text}")
			return response.text
		except requests.exceptions.RequestException as e:
			print(f"Error fetching {self.base_url}: {e}")
			return None

	def parse_product(self, html: str) -> Optional[Product]:
		soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

		# Explicitly type the elements
		name_element: Optional[Tag] = soup.find("h1")
		price_element: Optional[Tag] = soup.select_one(".price")

		# Handle None cases
		if not name_element or not price_element:
			return None

		# Type narrowing (mypy now knows these are Tags, not None)
		name: str = name_element.get_text(strip=True)
		price_str: str = price_element.get_text(strip=True)

		try:
			price: float = float(price_str.replace("$", "").replace(",", ""))
		except ValueError:
			return None

		return Product(name=name, price=price, url=self.base_url)