from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def setup(request):
    try:
        service = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        request.cls.driver = driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
    except Exception as e:
        print(f"Error occured: {e}")