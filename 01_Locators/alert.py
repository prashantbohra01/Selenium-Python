from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

validateKeys = "Prashant"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(validateKeys)
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text

assert validateKeys in alertText
alert.accept()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(validateKeys)
driver.find_element(By.ID,"confirmbtn").click()

alert.dismiss()
input("ENter ")