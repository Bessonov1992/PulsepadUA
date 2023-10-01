from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class WelcomePage:
    __URL = "https://pulsepad.com.ua/"

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.category_xpath = '//span[contains(@class,"header__menu-catalog-list-item-link level_1")]'
        self.finder_xpath = '//input[@name="keyword"]'

    def open(self):
        self.__driver.get(self.__URL)

    def find_all_categories(self) -> list:
        list_of_categories = []
        categories = self.__driver.find_elements(By.XPATH, self.category_xpath)
        for i in categories:
            categories_title = i.text
            list_of_categories.append(categories_title)
        return list_of_categories

    def count_all_categories(self) -> int:
        counter = 0
        categories = self.__driver.find_elements(By.XPATH, self.category_xpath)
        for _ in categories:
            counter += 1
        return counter
