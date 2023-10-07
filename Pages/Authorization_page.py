from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PulsepadAuthorization:
    __URL = 'https://pulsepad.com.ua'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.authorization_button_xpath = '//div[@class="account__link"]'
        self.auth_field_login_xpath = '//input[@name="popup_email"]'
        self.auth_field_pass_xpath = '//input[@name="popup_password"]'
        self.auth_button_enter = '//span[contains(text(),"Увійти")]'
        self.auth_favicon_nickname_xpath = '//span[@class="tablet-elem tablet-elem--inline"]'

    def open(self):
        self.__driver.get(self.__URL)

    def authorization(self, auth_data):
        element = self.__driver.find_element(By.XPATH, self.authorization_button_xpath)
        element.click()
        element = self.__driver.find_element(By.XPATH, self.auth_field_login_xpath)
        element.send_keys(auth_data[0])
        element = self.__driver.find_element(By.XPATH, self.auth_field_pass_xpath)
        element.send_keys(auth_data[1])
        element = self.__driver.find_element(By.XPATH, self.auth_button_enter)
        element.click()

    def is_authorizated(self, name: str) -> bool:
        auth_name = self.__driver.find_element(By.XPATH, self.auth_favicon_nickname_xpath).text
        if auth_name == name:
            return True
        else:
            return False
