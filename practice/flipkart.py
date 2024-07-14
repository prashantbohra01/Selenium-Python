from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('https://www.flipkart.com/')

driver.find_element(By.CLASS_NAME, "Pke_EE").send_keys("Mobiles")
driver.find_element(By.CLASS_NAME, "Pke_EE").send_keys(Keys.RETURN)

# Define the XPath expression
xpath = "//div[@class='Nx9bqj _4b5DiR' and number(translate(text(), '₹,', '')) < 20000]"

# Find the elements using the XPath expression
elements = driver.find_elements(By.XPATH, xpath)

# Print the text of each found element
for i in elements:
    print(i.text)

input("Enter ")

