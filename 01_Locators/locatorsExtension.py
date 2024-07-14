from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://login.salesforce.com/?locale=in")

# Generating CSS by ID
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("Prashant") 

# Generating CSS by ClassName
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("Prashant1241")
driver.find_element(By.CSS_SELECTOR, ".password").clear() # clears the text present in the input box

# Use of LinkText Locator

driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()

driver.find_element(By.NAME,"cancel").click()

# Creating XPATH by traversing tags
# Syntax :- //tagname[@attribute='value'/tagname/tagname]
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)


# Creating CSS by traversing tags
# Syntax :- tagname[attribute='value' tagname:nth-child(1)]
print(driver.find_element(By.CSS_SELECTOR, "form[name='login'] label:nth-child(4)").text)

input("Enter")