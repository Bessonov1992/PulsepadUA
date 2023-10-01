from Pages.Laptop_page import PulsepadLaptop


class TestLaptop:

    def test_count_items_on_page(self, chrome):
        page = PulsepadLaptop(chrome)
        page.open()
        assert page.count_items() <= 24

    def test_filter_works(self, chrome):
        page = PulsepadLaptop(chrome)
        page.open()
        page.choose_checkbox("LG")
        assert page.is_filter_works("LG")

    def test_checkbox(self, chrome):
        page = PulsepadLaptop(chrome)
        page.open()
        page.choose_checkbox("Samsung")
        assert page.is_checkbox_chosen("Samsung")
