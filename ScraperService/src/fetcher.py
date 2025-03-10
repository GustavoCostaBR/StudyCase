from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional
import os


class Fetcher:
	def __init__(self, url: str, class_name: str):
		self.url = url
		self.class_name = class_name
		self.chrome_options = Options()
		self.chrome_options.add_argument("--headless")  # Run in headless mode
		self.chrome_options.add_argument("--no-sandbox")
		self.chrome_options.add_argument("--disable-dev-shm-usage")
		self.chrome_options.add_argument("--disable-gpu")  # Disable GPU
		self.chrome_options.add_argument("--log-level=3")    # Suppress logging
		self.chrome_options.add_argument("--enable-unsafe-webgl")  # Enable unsafe WebGL
		self.chrome_options.add_argument(
			"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
			"(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
		)
		# Check environment for CHROMEDRIVER_PATH before using webdriver_manager.
		driver_path = os.environ.get("CHROMEDRIVER_PATH")
		try:
			if driver_path:
				print(f"Using ChromeDriver from environment: {driver_path}")
				# Explicitly set Chrome binary location.
				self.chrome_options.binary_location = "/usr/bin/google-chrome"
				self.service = Service(driver_path)
			else:
				print("No CHROMEDRIVER_PATH specified. Using webdriver_manager to install driver.")
				self.service = Service(ChromeDriverManager().install())
			self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

			# Print Chrome and ChromeDriver versions
			print(f"Chrome version: {self.driver.capabilities['browserVersion']}")
			print(f"ChromeDriver version: {self.driver.capabilities['chrome']['chromedriverVersion']}")

		except Exception as e:
			print(f"Error initializing WebDriver: {e}")
			raise  # Re-raise the exception to prevent further execution


	def fetch_html(self) -> Optional[str]:
		try:
			self.driver.get(self.url)
			WebDriverWait(self.driver, 20).until(
				EC.presence_of_all_elements_located((By.CLASS_NAME, self.class_name))
			)
			self.driver.save_screenshot('screenshot.png')
			html_content = self.driver.page_source
			return html_content
		except Exception as e:
			print(f"Error fetching {self.url}: {e}")
			return None
		finally:
			self.driver.quit()