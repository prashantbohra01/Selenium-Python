from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to chromedriver.exe
service = Service("C:\\chromedriver.exe")

# Create an instance of Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# CSS selector
# CSS Syntax = tagname[attribute='value']

# Regular Exp - [attribute*='value'] 
# for example - [class*='alert-success']

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Prashant")

# Xpath Selector
# Xpath Syntax = //tagname[@attribute='value']

# Regular Exp - //*[contains(@attribute,'value')]
# for example - //*[contains(@class,'alert-success')]

driver.find_element(By.XPATH,"//input[@type='submit']").click()

message = driver.find_element(By.XPATH, "//*[contains(@class,'alert-success')]").text
print(message)


# Assertion looks for expected values, if it does not recieve expected value then it fails. 
# Assert always expects true condition.
assert 'success' in message

input("Press Enter ")