from scraper import Scraper
from config import BASE_URL
from config import SEARCH_URL
from config import DIV_PRODUCT_DETAILS_CLASS

url = BASE_URL
searchUrl = SEARCH_URL
div_class = DIV_PRODUCT_DETAILS_CLASS

class_name = "stamp--caption-wrapper-title"

def get_user_input(prompt: str) -> str:
    """
    Get a strongly typed input from the user.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The user's input as a string.
    """
    return input(prompt)

term = get_user_input("Enter the search term/product: ")

scraper = Scraper(searchUrl + term, class_name)
result = scraper.scrape()

if result:
    print(f"Found content: {result}")
else:
    print("Content not found.")