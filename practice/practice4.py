# Task 3 = Verify search functionality in home page is working.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

validate = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

wait = WebDriverWait(driver, 7)
wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='products']/div")))

values = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")

validation=[i.text for i in values]

print(validation)

assert validate == validation

print("Passed")

