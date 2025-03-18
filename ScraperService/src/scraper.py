from typing import Optional
from src.fetcher import Fetcher
from src.parser import Parser
from src.models import Product


class Scraper:
	def __init__(self, url: str, class_name: str, pool):
		self.url = url
		self.class_name = class_name
		self.fetcher = Fetcher(url, class_name, pool)
		self.parser = Parser(class_name)

	def scrape(self) -> Optional[str]:
		html = self.fetcher.fetch_html()
		if html:
			return self.parser.parse_multiple(html)
		return None

	def searchAndScrape(self) -> Optional[str]:
		html = self.fetcher.fetch_html()
		if html:
			return self.parser.parse_products(html)
		return None