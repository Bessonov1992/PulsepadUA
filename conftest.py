import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import auth
from Pages.Authorization_page import PulsepadAuthorization


@pytest.fixture(scope="class")
def chrome():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def authorization():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    page = PulsepadAuthorization(driver)
    page.open()
    page.authorization(auth.auth_data)
    with open("cookies.py", "w") as file:
        cookies = driver.get_cookies()
        file.write(f'cookies={cookies}')
    yield driver
    driver.quit()
