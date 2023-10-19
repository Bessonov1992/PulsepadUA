from Pages.Authorization_page import PulsepadAuthorization
from auth import auth_data


class TestLaptop:

    def test_authorization(self, chrome):
        page = PulsepadAuthorization(chrome)
        page.open()
        page.authorization(auth_data)
        page.open()
        assert page.is_authorizated("Дмитро")
