from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://uitestingplayground.com/textinput'
driver = webdriver.Chrome()
driver.get(url)

input_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, 'newButtonName'))
)
input_field.send_keys('SkyPro')

button = driver.find_element(By.ID, 'updatingButton')
button.click()
button_text = button.text
print(button_text)

driver.quit()
