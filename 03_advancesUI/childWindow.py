
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.XPATH,"//div[@class='example']/a").click()

childWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)

print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])

print(driver.find_element(By.TAG_NAME,"h3").text)

input("Enter ")