from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Use programcreep.com to know more about chrome options


service = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)