import pytest

from Pages.Welcome_page import WelcomePage

list_of_expected_categories = ["Телефони та Аксесуари", "Зарядні станції", "Електросамокати",
                               "Смарт-годинник та браслети", "Автоелектроніка", "Фото та Відео", "Екшн камери",
                               "Комп'ютерна техніка", "ТБ, Аудіо, Відео", "Квадрокоптери", "Ігрові приставки",
                               "Побутова техніка та інтер'єр", "Гіроскутери, гіроборди", "Пилососи, Роботи-пилососи",
                               "Дитячі конструктори", "Аксесуари Xiaomi", "Генератори", "Спорт, Активний відпочинок"]


class TestWelcomePage:
    def test_all_categories_exist(self, chrome):
        page = WelcomePage(chrome)
        page.open()
        assert page.find_all_categories() == list_of_expected_categories and page.count_all_categories() == 18
