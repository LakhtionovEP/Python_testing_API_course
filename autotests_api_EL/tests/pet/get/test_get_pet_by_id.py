import pytest
import allure


@pytest.mark.parametrize("pet_id", [1])
def test_positive(base_fixture, pet_id):
    with allure.step("Выполнение запроса"):
        response = base_fixture.api.get_pet_by_id(pet_id)
        resp_dict = response.json()

    with allure.step("Проверка ответа."):
        assert response.status_code == 200, "Код ответа не соответствует ожидаемому."

        check_resp = base_fixture.checker.validate_json(resp_dict, "get_by_pet_id_response.json")
        assert check_resp is True, "тело ответа не соответствует схеме pet.json"

        if "id" in resp_dict:
            assert resp_dict["id"] == pet_id, f"id не соответствует ожидаемому exp={pet_id} actual={resp_dict['id']}"