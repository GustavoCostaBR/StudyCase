from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Disable GPU
chrome_options.add_argument("--log-level=3")  # Suppress logging
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")


# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
	# Fetch the URL
	driver.get("https://nakup.itesco.cz/groceries/en-GB")

	# Wait for the page to load completely
	# driver.implicitly_wait(10)
	WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "stamp--caption-wrapper-title"))
    )

	# Get the page source
	html_content = driver.page_source
	soup = BeautifulSoup(html_content, 'html.parser')

	# Find all <h3> elements with the class 'stamp--caption-wrapper-title'
	h3_elements = soup.find_all('h3', class_='stamp--caption-wrapper-title')

	# Print the contents of each found element
	for h3 in h3_elements:
		print(h3.get_text())

	driver.save_screenshot('screenshot.png')


finally:
	# Close the WebDriver
	driver.quit()