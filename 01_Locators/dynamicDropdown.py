from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# code starts here
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)


# find_elements is used to get A list of WebElement objects.
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break

assert driver.find_element(By.ID,"autosuggest").get_attribute('value') == "India"

input("enter")