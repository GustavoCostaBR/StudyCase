from scraper import Scraper
from config import BASE_URL


url = BASE_URL
class_name = "stamp--caption-wrapper-title"

scraper = Scraper(url, class_name)
result = scraper.scrape()

if result:
    print(f"Found content: {result}")
else:
    print("Content not found.")