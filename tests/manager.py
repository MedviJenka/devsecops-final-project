from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--headless"),
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")


class DriverManager:

    def __init__(self, headless: bool = False) -> None:
        self.driver = webdriver.Chrome(options=chrome_options) if headless else webdriver.Chrome()
=======
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverManager:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
>>>>>>> 7b6ffe2 (tests)

    def open_url(self, url: str) -> None:
        self.driver.get(url)

<<<<<<< HEAD
    def get_element(self, by: str, element_name: str) -> WebElement:
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((by, element_name)))
=======
    def get_element(self, by: str, element_name: str):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located((by, element_name))
        )
>>>>>>> 7b6ffe2 (tests)
