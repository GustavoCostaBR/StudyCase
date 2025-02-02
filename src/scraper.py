from typing import Optional
from fetcher import Fetcher
from parser import Parser
from models import Product


class Scraper:
    def __init__(self, url: str, class_name: str):
        self.url = url
        self.class_name = class_name
        self.fetcher = Fetcher(url, class_name)
        self.parser = Parser(class_name)

    def scrape(self) -> Optional[str]:
        html = self.fetcher.fetch_html()
        if html:
            return self.parser.parse_multiple(html)
        return None