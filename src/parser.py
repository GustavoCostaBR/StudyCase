from typing import Optional
from bs4 import BeautifulSoup

class Parser:
	def __init__(self, class_name: str):
		self.class_name = class_name

	def parse_multiple(self, html: str) -> Optional[list[str]]:
		soup = BeautifulSoup(html, "html.parser")
		elements = soup.findAll(class_=self.class_name)
		if elements:
			return [element.get_text(strip=True) for element in elements]
		return None

	def parse_single(self, html: str, tag: str) -> Optional[str]:
		soup = BeautifulSoup(html, "html.parser")
		element = soup.find(tag, class_=self.class_name)
		if element:
			return element.get_text(strip=True)
		return None