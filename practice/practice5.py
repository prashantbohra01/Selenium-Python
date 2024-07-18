from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
   productName = product.find_element(By.XPATH,"div/h4/a").text

   if productName == "Blackberry":
      print(productName)
      print("Buy this Product")
      product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

validate = driver.find_element(By.CSS_SELECTOR,"h4.media-heading").text

assert validate == "Blackberry"
print("Passed")

driver.find_element(By.CSS_SELECTOR,".btn-success").click()

driver.find_element(By.ID,"country").send_keys("India")

# Implement Explicit wait here

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='suggestions'] ul li")))
driver.find_element(By.CSS_SELECTOR,"div[class='suggestions'] ul li").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

successText = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

assert "Success! Thank you!" in successText
print("Success alert passed")

driver.get_screenshot_as_file("screen.png")

input("Enter: ")