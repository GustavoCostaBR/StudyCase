from typing import Optional
from bs4 import BeautifulSoup
import re
from datetime import datetime
from models import Product
import config as cfg

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

	def parse_products(self, html: str) -> Optional[list[Product]]:
		soup = BeautifulSoup(html, "html.parser")
		productUiList = soup.findAll(class_=self.class_name)
		if productUiList:
			products = []
			for productUi in productUiList:
				nameElement = productUi.find(class_ = cfg.SPAN_PRODUCT_NAME_CLASS)
				if nameElement:
					name = nameElement.get_text(strip=True)
				else:
					continue

				pricePerUnit, pricePerKg, clubCardPrice, offerPrice = self.extractPrice(productUi)

				offerDatesElement = productUi.find(class_=cfg.SPAN_CLASS_OFFER_DATES)
				if offerDatesElement:
					offerDatesText = offerDatesElement.get_text(strip=True)
					offerDate = self.extractOfferDate(offerDatesText)
				else:
					offerDate = datetime.min

				clubCardOfferDatesElement = productUi.find(class_=cfg.SPAN_CLASS_CLUBCARD_OFFER_DATES)
				if clubCardOfferDatesElement:
					clubCardOfferDatesText = clubCardOfferDatesElement.get_text(strip=True)
					clubCardOfferDate = self.extractOfferDate(clubCardOfferDatesText)
				else:
					clubCardOfferDate = datetime.min

				if (pricePerUnit == -10.00) and (pricePerKg == -10.00) and (clubCardPrice == -10.00) and (offerPrice == -10.00):
					continue

				product = Product(
					Name=name, Price=pricePerUnit, PricePerKg=pricePerKg, OfferPrice=offerPrice, OfferPriceClubCard=clubCardPrice, DateOfOffer=offerDate, DateOfOfferClubCard=clubCardOfferDate, Url="Unknown")
				products.append(product.model_dump())

			return products
		return None

	def extractPrice(self, productUi) -> Optional[tuple[float, float, float, float]]:
		pricePerUnitElement = productUi.find(class_ = cfg.P_CLASS_PRICE_PER_UNIT)
		if pricePerUnitElement:
			pricePerUnitText = pricePerUnitElement.get_text(strip=True)
			pricePerUnitMatch = re.search(r"[\d,]+", pricePerUnitText)
			if pricePerUnitMatch:
				price_str = pricePerUnitMatch.group(0).replace(",", ".")
				pricePerUnit = float(price_str)
			else:
				pricePerUnit = -10.00
		else:
			pricePerUnit = -10.00

		pricePerKgElement = productUi.find(class_ = cfg.P_CLASS_PRICE_PER_KG)
		if pricePerKgElement:
			pricePerKgText = pricePerKgElement.get_text(strip=True)
			price_match = re.search(r"[\d,]+", pricePerKgText)
			if price_match:
				price_str = price_match.group(0).replace(",", ".")
				pricePerKg = float(price_str)
			else:
				pricePerKg = -10.00
		else:
			pricePerKg = -10.00

		clubCardPriceElement = productUi.find(class_=cfg.P_CLUBCARD_PRICE_CLASS)
		if clubCardPriceElement:
			clubCardPriceText = clubCardPriceElement.get_text(strip=True)

			clubCardPriceMatch = re.search(r"Clubcard\s([\d,]+)", clubCardPriceText)
			if clubCardPriceMatch:
				price_str = clubCardPriceMatch.group(1).replace(",", ".")
				clubCardPrice = float(price_str)
			else:
				clubCardPrice = -10.00
		else:
			clubCardPrice = -10.00

		offerPriceElement = productUi.find(class_=cfg.SPAN_OFFER_PRICE_CLASS)
		if offerPriceElement:
			offerPriceText = offerPriceElement.get_text(strip=True)
			offerPriceMatches = re.findall(r"([\d,]+)", offerPriceText)
			if offerPriceMatches:
		# Select the last price
				price_str = offerPriceMatches[-1].replace(",", ".")
				offerPrice = float(price_str)
			else:
				offerPrice = -10.00
		else:
			offerPrice = -10.00

		return pricePerUnit, pricePerKg, clubCardPrice, offerPrice


	def extractOfferDate(self, text: str) -> Optional[datetime]:
		# Use regular expression to find the date pattern
		date_match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
		if date_match:
			date_str = date_match.group(1)
			return datetime.strptime(date_str, "%d/%m/%Y")
		return datetime.min