from src.models import Product 
from src.scraper import Scraper
from src.apiCaller import APICaller
from src.config import BASE_URL, SEARCH_URL, DIV_PRODUCT_DETAILS_CLASS

class ScraperService:
    """
    A service class to perform scraping based on a search term.
    """
    BASE_URL = BASE_URL
    SEARCH_URL = SEARCH_URL
    DIV_PRODUCT_DETAILS_CLASS = DIV_PRODUCT_DETAILS_CLASS

    @classmethod
    def search(cls, search_term: str) -> None:
        """
        Perform the scraping based on the given search term and send the result to the API.

        Args:
            search_term (str): The search term or product query.
        """
        scraper = Scraper(cls.SEARCH_URL + search_term, cls.DIV_PRODUCT_DETAILS_CLASS)
        products = scraper.searchAndScrape()
        
        if products:
            # Convert each dictionary to a Product object
            products = [Product(**product_data) for product_data in products]
            APICaller.send_products(products)
            print("Content sent to API")
        else:
            print("Content not found.")
