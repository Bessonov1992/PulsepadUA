from Pages.Authorization_page import PulsepadAuthorization


class TestLaptop:
    auth_data = ["bessonov.dmitriy92@gmail.com", "Qwerty123"]

    def test_authorization(self, chrome):
        page = PulsepadAuthorization(chrome)
        page.open()
        page.authorization(self.auth_data)
        page.open()
        assert page.is_authorizated("Дмитро")
