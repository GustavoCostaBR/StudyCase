from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional
import os
from src.driverPool import DriverPool


class Fetcher:
    def __init__(self, url: str, class_name: str, pool):
        self.url = url
        self.class_name = class_name
        self.pool = pool

    def fetch_html(self) -> Optional[str]:
        driver = self.pool.get_driver()
        try:
            driver.get(self.url)
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.class_name))
            )
            html_content = driver.page_source
            return html_content
        except Exception as e:
            print(f"Error fetching {self.url}: {e}")
            return None
        finally:
            self.pool.return_driver(driver)