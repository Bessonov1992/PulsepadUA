import json

from Api_methods import API_helper_methods
from Api_methods.Pet_store_api_methods import Pet


class TestPet:
    def test_post_pet_status_200(self):
        method = Pet()
        body = API_helper_methods.create_body()
        answer = method.post_pet(body)
        assert answer.status_code == 200
        method.dell_pet(178)

    def test_compare_post_data_with_db(self):
        method = Pet()
        body = API_helper_methods.create_body()
        answer = method.post_pet(body)
        try:
            assert answer.text == method.get_pet_by_id(178).text
        except AssertionError:
            if answer.status_code == 200:
                method.dell_pet(178)
            raise AssertionError

    def test_pet_id_equal_str(self):
        method = Pet()
        body = API_helper_methods.create_body(pet_id="wrong")
        answer = method.post_pet(body)
        try:
            assert answer.status_code == 400 and "error" in answer.text
        except AssertionError:
            if answer.status_code == 200:
                method.dell_pet(178)
            raise AssertionError

    def test_try_to_find_deleted_pet(self):
        method = Pet()
        body = API_helper_methods.create_body()
        method.post_pet(body)
        method.dell_pet(178)
        answer = method.get_pet_by_id(178)
        assert answer.status_code == 404 and "Pet not found" == answer.text

    def test_update_pet_info(self):
        method = Pet()
        body = API_helper_methods.create_body()
        method.post_pet(body)
        update_body = API_helper_methods.create_body(pet_name="Vasilisa")
        method.update_pet(update_body)
        answer = json.loads(method.get_pet_by_id(178).text)
        assert answer == update_body
        method.dell_pet(178)
