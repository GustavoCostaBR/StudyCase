# program.py
import sys
import os
from typing import Optional

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.scraper import PriceScraper
except ImportError:
    print("Error: Make sure your project structure is correct!")
    sys.exit(1)

def main():
    # Initialize scraper with a test URL
    # test_url = "http://example.com"  # Replace with your target URL
    scraper = PriceScraper()

    # Fetch HTML
    html: Optional[str] = scraper.fetch_html()

    if html:
        print("Successfully fetched HTML:\n")
        print(html[:2000] + "\n...")  # Print first 2000 chars to avoid flooding
    else:
        print("Failed to fetch HTML content")

if __name__ == "__main__":
    main()