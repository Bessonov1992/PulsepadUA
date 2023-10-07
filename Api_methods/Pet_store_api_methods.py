import requests


class Pet:
    def __init__(self):
        self.__post_create_pet = 'https://petstore3.swagger.io/api/v3/pet'
        self.__get_pet_by_id = 'https://petstore3.swagger.io/api/v3/pet/{}'
        self.__delete_pet_by_id = 'https://petstore3.swagger.io/api/v3/pet/{}'
        self.__update_pet = "https://petstore3.swagger.io/api/v3/pet"

    def post_pet(self, body):
        return requests.post(self.__post_create_pet, json=body)

    def dell_pet(self, pet_id):
        return requests.delete(self.__delete_pet_by_id.format(pet_id))

    def get_pet_by_id(self, pet_id):
        return requests.get(self.__get_pet_by_id.format(pet_id))

    def update_pet(self, body):
        return requests.put(self.__update_pet,json=body)
