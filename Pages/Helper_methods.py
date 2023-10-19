from Tests.cookies import cookies

from selenium.webdriver.remote.webdriver import WebDriver


def add_cookies_and_refresh(driver: WebDriver):
    for cookie in cookies:
        driver.add_cookie(cookie)
