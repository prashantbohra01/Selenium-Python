from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

action = ActionChains(driver)
dbl = driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
action.double_click(dbl).perform()

alert = driver.switch_to.alert
assert "You double clicked me.. Thank You.." == alert.text
alert.accept()

input("Enter: ")