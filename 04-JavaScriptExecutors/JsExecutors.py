from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.NAME, "name").send_keys("Hello")
# driver.find_element(By.NAME, "name").text   # We can not grab the text from input after sending it by selenium by text method.

print(driver.find_element(By.NAME, "name").get_attribute("value"))

# We can also use JavaScript DOM to grab the text 

print(driver.execute_script("return document.getElementsByName('name')[0].value"))

# We can use javascript executor when a feature is not working in selenium like click().

button = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

driver.execute_script("arguments[0].click();", button)

# how to scroll down a page using javascript executor because selenium does'nt support scroll

driver.execute_script("window.scrollTo(0, 500);")
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
input("Enter: ")