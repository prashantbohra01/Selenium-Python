
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# frame, iframe, frameset

driver.get("https://the-internet.herokuapp.com/iframe")

# frameid, framename, index value
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am automated")

driver.switch_to.default_content()
