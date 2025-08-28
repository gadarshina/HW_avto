from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.URL)

    @allure.step("Установка задержки {value} секунд")
    def enter_delay(self, value):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param value: int или str - время задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(value))

    @allure.step("Ввод чисел и операции: 7 + 8 =")
    def click_element(self):
        """
        Выполняет операцию 7 + 8 = на калькуляторе.
        """
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Ожидание результата '15' в дисплее")
    def wait_for_result(self, expected_result="15", timeout=60):
        """
        Ожидает появления ожидаемого результата в дисплее калькулятора.

        :param expected_result: str - ожидаемый результат.
        :param timeout: int - время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_result
            )
        )

    def get_result(self):
        """
        Получает текущий текст из дисплея калькулятора.

        :return: str - текущий результат.
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
