# Task 2 = To verify that the price decreases on applying promocode


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

wait = WebDriverWait(driver, 7)
wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='products']/div")))
# time.sleep(1)

buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# get value before applying promocode
# time.sleep(2)

wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoCode")))
Original_amount = driver.find_element(By.CSS_SELECTOR,"span.discountAmt").text
print(Original_amount)

# Apply promocode
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# get total amount after applying promocode
# time.sleep(7)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

dicounted_amount = driver.find_element(By.CSS_SELECTOR,"span.discountAmt").text
print(dicounted_amount)

assert dicounted_amount < Original_amount

print("Passed")

input("Enter: ")

