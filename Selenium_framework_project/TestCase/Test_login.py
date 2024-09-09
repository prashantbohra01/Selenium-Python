from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
import pytest
from PageObjects.LoginPage import Login

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_001(self):
        time.sleep(3)
        lg = Login(self.driver)
        lg.input_username("Admin")
        #self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin")
        lg.input_password("admin123")
        #self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin123")

        lg.login_button()
        #self.driver.find_element(By.CLASS_NAME, "oxd-button").click()
        time.sleep(2)

    def test_002(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Amin")
        self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin123")

        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()

        time.sleep(2)
        if "Invalid credentials" in self.driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text:
            assert True
        else:
            assert False
    def test_003(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin1234")

        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()

        time.sleep(2)
        if "Invalid credentials" in self.driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text:
            assert True
        else:
            assert False
