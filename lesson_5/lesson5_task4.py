from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")

    print(success_message.text.strip())
finally:
    driver.quit()