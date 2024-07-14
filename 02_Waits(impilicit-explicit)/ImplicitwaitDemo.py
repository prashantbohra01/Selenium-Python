from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Implicit wait 
# Waits until 5 seconds if object is not displayed
# Global wait
# 1.5 seconds to reach next page - execution will resume in 1.5 seconds
# if object do not show up at all, then max time your test waits for 5 seconds 
driver.implicitly_wait(5) 

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//div[@class='products']/div[1]/div[3]/button[1]").click()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(3) #(Python own wait not seleniums)

buttons = driver.find_elements(By.XPATH, "//div[@class='products']/div/div[3]/button")

for i in buttons:
    i.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
input("Enter ")