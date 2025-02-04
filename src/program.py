from scraper import Scraper
import yaml
from config import BASE_URL
from config import SEARCH_URL
from config import DIV_PRODUCT_DETAILS_CLASS

url = BASE_URL
searchUrl = SEARCH_URL
div_class = DIV_PRODUCT_DETAILS_CLASS

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

scraper = Scraper(searchUrl + term, div_class)
result = scraper.searchAndScrape()


with open('products.yaml', 'w') as file:
    yaml.dump(result, file)

if result:
    print(f"Found content: {result}")
else:
    print("Content not found.")