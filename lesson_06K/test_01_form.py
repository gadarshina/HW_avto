import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Для Safari обычно достаточно просто создать драйвер без дополнительных настроек
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_but(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

    # Zip code оставить пустым
    zip_code_input = driver.find_element(By.NAME, "zipCode")
    zip_code_input.clear()

    # Остальные поля
    driver.find_element(By.NAME, "city").send_keys("Москва")

    # Выбор страны (Россия)
    country_select = wait.until(EC.element_to_be_clickable((By.NAME, "country")))
    country_select.click()
    country_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Россия']")))
    country_option.click()

    # Выбор должности (QA)
    job_select = wait.until(EC.element_to_be_clickable((By.NAME, "jobPosition")))
    job_select.click()
    job_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='QA']")))
    job_option.click()

    # Компания
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    submit_button.click()

    def get_field_border_color(field):
        return field.value_of_css_property('border-color')

    def is_red(color_value):
        return color_value in ['rgb(255, 0, 0)', 'rgba(255, 0, 0, 1)']

    def is_green(color_value):
        return color_value in ['rgb(0, 128, 0)', 'rgba(0, 128, 0, 1)']

    # Проверка подсветки поля Zip code (должно быть красным)
    zip_code_field = driver.find_element(By.NAME, "zipCode")

    # Ждем появления красного цвета границы
    wait.until(lambda d: is_red(get_field_border_color(zip_code_field)))

    assert is_red(get_field_border_color(zip_code_field)), "Zip code поле не подсвечено красным"

    # Проверка остальных полей (должны быть зелеными)
    other_fields_names = [
        "firstName",
        "lastName",
        "address",
        "email",
        "phone",
        "city",
        "country",
        "jobPosition",
        "company"
    ]

    for name in other_fields_names:
        field = driver.find_element(By.NAME, name)
        # Ждем появления зеленого цвета границы
        wait.until(lambda d: is_green(get_field_border_color(field)))
        color = get_field_border_color(field)
        assert is_green(color), f"Поле {name} не подсвечено зеленым"