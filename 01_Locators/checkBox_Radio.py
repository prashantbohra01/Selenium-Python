from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes= driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for i in checkboxes:
    if i.get_attribute('value')=='option2':
        i.click()
        assert i.is_selected()

driver.find_element(By.XPATH, "//input[@value='radio3']").click()

input("enter ")