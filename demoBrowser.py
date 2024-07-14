from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver.exe
service = Service("C:\\chromedriver.exe")

# Create an instance of Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get("https://www.selenium.dev/")

print(driver.title)
print(driver.current_url)
driver.get("https://www.selenium.dev/downloads/")
driver.back()
driver.close()