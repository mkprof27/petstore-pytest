import requests
import pytest
import allure
from config.settings import BASE_URL

@allure.epic("Petstore API")
@allure.feature("Питомцы")
class TestPet:

    @allure.title("Создание питомца")
    def test_created_pet(self, created_pet):
        assert created_pet["id"] == 72200
        assert created_pet["name"] == "Барсик"

    @allure.title("Обновление питомца")
    def test_update_pet(self, created_pet):
        with allure.step("Отправляем PUT запрос"):
            payload_update = {
                "id": 72200,
                "name": "Мурзик",
                "status": "sold",
                "photoUrls": ["string"]
            }
            response = requests.put(f"{BASE_URL}/pet", json=payload_update)
        with allure.step("Проверяем ответ"):
            assert response.status_code == 200
            assert response.json()["name"] == "Мурзик"

    @allure.title("Удаление питомца")
    def test_delete_pet(self, created_pet):
        response = requests.delete(f"{BASE_URL}/pet/{created_pet['id']}")
        assert response.status_code == 200

    @allure.title("Создание питомца с разными статусами")
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_create_pet_status(self, status):
        payload = {"name": "Барсик", "status": status, "photoUrls": []}
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()["status"] == status