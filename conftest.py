import requests
import pytest
from config.settings import BASE_URL

@pytest.fixture
def created_pet():
    payload = {
        "id": 72200,
        "category": {"id": 0, "name": "cats"},
        "name": "Барсик",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    pet = response.json()
    yield pet
    requests.delete(f"{BASE_URL}/pet/{pet['id']}")