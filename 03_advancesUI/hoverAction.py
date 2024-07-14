
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

action = ActionChains(driver)
menu = driver.find_element(By.ID,"mousehover")
action.move_to_element(menu).perform()

childMenu = driver.find_element(By.LINK_TEXT,"Top")
action.move_to_element(childMenu).click().perform()