# Task 3 = verify if sum of products in checkout page matches with total amount

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


wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promoCode")))

# get the sum of all items 

amounts = driver.find_elements(By.XPATH, "//table[@class='cartTable']/tbody/tr/td[5]/p")

sum = 0

for amount in amounts:
    sum = sum + int(amount.text)
    print(amount.text)

print("sum of all the items is : " + str(sum))

# get value of total amount
Original_amount = driver.find_element(By.CSS_SELECTOR,"span.discountAmt").text
print("original amount is :"+ str(Original_amount))

assert str(sum) == str(Original_amount)
print("Passed")

input("Enter: ")

