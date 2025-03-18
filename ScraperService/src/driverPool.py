import os
import queue
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverPool:
    def __init__(self, pool_size: int):
        self.pool = queue.Queue(maxsize=pool_size)
        for _ in range(pool_size):
            driver = self._create_driver()
            self.pool.put(driver)
    
    def _create_driver(self) -> webdriver.Chrome:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--enable-unsafe-webgl")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
        # Check for a pre-installed ChromeDriver via env variable.
        driver_path = os.environ.get("CHROMEDRIVER_PATH")
        if driver_path:
            chrome_options.binary_location = "/usr/bin/google-chrome"
            service = Service(driver_path)
        else:
            service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def get_driver(self):
        return self.pool.get()
    
    def return_driver(self, driver):
        self.pool.put(driver)
    
    def shutdown(self):
        while not self.pool.empty():
            driver = self.pool.get()
            driver.quit()