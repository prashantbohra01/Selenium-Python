# Task 1 = To validate whether products selected in page 1 are showing in page 2


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

list = []
list2 = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("Ber")
# wait = WebDriverWait(driver, 3)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-name')))
time.sleep(1)

elements = driver.find_elements(By.CSS_SELECTOR, "h4.product-name")
for element in elements:
    list.append(element.text)

print(list)

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for i in buttons:
    i.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(2)

wait = WebDriverWait(driver, 7)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'p.product-name')))
el = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for i in el:
    list2.append(i.text)

print(list2)

assert list == list2

input("Enter") 

