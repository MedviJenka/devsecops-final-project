from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverManager:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def get_element(self, by: str, element_name: str):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located((by, element_name))
        )
