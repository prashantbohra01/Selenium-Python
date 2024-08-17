import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#command line browser invocation
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://rahulshettyacademy.com/angularpractice")

    elif browser_name == "firefox":
        service = Service("")
        driver = webdriver.Firefox(service=service)
        driver.get("https://rahulshettyacademy.com/angularpractice")

    elif browser_name == "IE":
        #IE invocation code
        driver.get("https://rahulshettyacademy.com/angularpractice")

    request.cls.driver = driver

    yield 
    driver.close()