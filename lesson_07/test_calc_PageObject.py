import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_locator = (By.ID, "result")

    def enter_delay(self, value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)


    def click_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH, f"//button[text()='{button_text}']"
        )
        button.click()

    def get_result(self):
        result_element = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(self.result_locator)
        )
        return result_element.text


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = CalculatorPage(driver)
    calculator.enter_delay("45")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    result = calculator.get_result()
    assert result == "15"
