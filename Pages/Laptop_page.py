from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PulsepadLaptop:
    __URL = "https://pulsepad.com.ua/catalog/noutbuki"

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__item_xpath = '//a[@class="product-preview__name-link"]'
        self.__filter_checkbox_name_xpath = '//span[text()="{}"]'
        self.__filter_checkbox_xpath = '//span[text()="{}"]/ancestor::button'

    def open(self):
        self.__driver.get(self.__URL)

    def count_items(self) -> int:
        counter = 0
        for _ in self.__driver.find_elements(By.XPATH, self.__item_xpath):
            counter += 1
        return counter

    def choose_checkbox(self, name: str):
        checkbox = self.__driver.find_element(By.XPATH, self.__filter_checkbox_name_xpath.format(name))
        checkbox.click()

    def is_filter_works(self, name: str) -> bool:
        for i in self.__driver.find_elements(By.XPATH, self.__item_xpath):
            if name not in i.text:
                return False
            return True

    def is_checkbox_chosen(self, name: str) -> bool:
        checkbox_class = self.__driver.find_element(By.XPATH, self.__filter_checkbox_xpath.format(name)).get_attribute(
            "class")
        if "checked" in checkbox_class:
            return True
        else:
            return False
