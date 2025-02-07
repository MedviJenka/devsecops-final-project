import pytest
from selenium import webdriver
from selenium.common import TimeoutException
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 7b6ffe2 (tests)
=======

>>>>>>> 7b6ffe2 (tests)
=======

>>>>>>> 7b6ffe2 (tests)
from tests.manager import DriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def driver() -> webdriver:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    manager = DriverManager(headless=True)
=======
    manager = DriverManager()
>>>>>>> 7b6ffe2 (tests)
=======
    manager = DriverManager()
>>>>>>> 7b6ffe2 (tests)
=======
    manager = DriverManager()
>>>>>>> 7b6ffe2 (tests)
    manager.open_url('http://localhost:89')
    return manager


class TestFrontend:

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    """these tests test the main application functionality and also the BE in parallel"""

    def test_click_on_button_with_no_text_raise_popup(self, driver) -> None:
        driver.get_element(by=By.XPATH, element_name='/html/body/div/form/button').click()
        with pytest.raises(TimeoutException):
            driver.get_element(by=By.XPATH, element_name='/html/body/div/div')

=======
>>>>>>> 7b6ffe2 (tests)
=======
>>>>>>> 7b6ffe2 (tests)
=======
>>>>>>> 7b6ffe2 (tests)
    def test_main_screen(self, driver) -> None:
        result = driver.get_element(by=By.XPATH, element_name='/html/body/div/h1').text
        assert 'Roast Bot' in result

    def test_gif_exists(self, driver) -> None:
        result = driver.get_element(by=By.XPATH, element_name='/html/body/div/img')
        assert result

    def test_response(self, driver) -> None:
        driver.get_element(by=By.NAME, element_name='user_input').send_keys('hello')
        driver.get_element(by=By.XPATH, element_name='/html/body/div/form/button').click()
        result = driver.get_element(by=By.XPATH, element_name='/html/body/div/div').text
        assert 'AI:' in result
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7b6ffe2 (tests)
=======
>>>>>>> 7b6ffe2 (tests)

    def test_click_on_button_with_no_text_raise_popup(self, driver) -> None:
        driver.get_element(by=By.XPATH, element_name='/html/body/div/form/button').click()
        with pytest.raises(TimeoutException):
            driver.get_element(by=By.XPATH, element_name='/html/body/div/div')
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7b6ffe2 (tests)
=======
>>>>>>> 7b6ffe2 (tests)
=======
>>>>>>> 7b6ffe2 (tests)
