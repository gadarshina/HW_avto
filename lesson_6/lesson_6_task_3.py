from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver. Chrome()
waiter = WebDriverWait(driver, 120)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

waiter.until(
    EC.presence_of_element_located((By.TAG_NAME, "img"))
)
images = driver. find_elements(By.TAG_NAME,"img")
images_src = images[2].get_attribute("src")

print(images_src)

driver.quit()
