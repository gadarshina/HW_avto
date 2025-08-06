from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Укажите путь к вашему драйверу, например chromedriver
driver_path = 'path/to/chromedriver'

# Создаем экземпляр браузера
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Переходим на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода по его id
    input_field = driver.find_element(By.ID, "textInput")

    # Вводим текст "SkyPro"
    input_field.send_keys("SkyPro")

    # Находим синюю кнопку по её классу или тексту
    # Предположим, что это кнопка с классом btn-primary
    button = driver.find_element(By.CLASS_NAME, "btn-primary")

    # Нажимаем на кнопку
    button.click()

    # Получаем текст кнопки после клика
    button_text = button.text

    # Выводим в консоль в нужном формате
    print(f'"{button_text}"')

finally:

    time.sleep(2)
    driver.quit()