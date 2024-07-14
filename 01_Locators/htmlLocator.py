from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Specify the path to chromedriver.exe
service = Service("C:\\chromedriver.exe")

# Create an instance of Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#Using name locator
driver.find_element(By.NAME,"name").send_keys("Prashant")
driver.find_element(By.NAME,"email").send_keys("prashant@gmail.com")

#Using ID locator
driver.find_element(By.ID,"exampleInputPassword1").send_keys("prashant123")
driver.find_element(By.ID,"exampleCheck1").click()

# Static DropDown Select
# Select class provide the methods to handle the options in dropdown.
# It can be only used when Select tag is present.

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@type='submit']").click()

print(driver.find_element(By.XPATH, "//*[contains(@class,'alert-success')]").text)

input("press enter")
