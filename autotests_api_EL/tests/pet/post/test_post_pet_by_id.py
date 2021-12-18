import pytest
import allure


#@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_positive(base_fixture):
    with allure.step("Выполнение запроса"):
        id, category_id, category, name, photoUrls, tags_id, tags, status = base_fixture.helper.create_pet()
        response = base_fixture.api.post_pet(id, category_id, category, name, photoUrls, tags_id, tags)
        resp_dict = response.json()

    with allure.step("Проверка ответа."):
        assert response.status_code == 200, "Код ответа не соответствует ожидаемому."

        check_resp = base_fixture.checker.validate_json(resp_dict, "post_pet_by_id.json")
        assert check_resp is True, "тело ответа не соответствует схеме pet.json"

        if "id" in resp_dict:
            assert resp_dict["id"] == base_fixture.pet_id, f"id не соответствует ожидаемому exp={base_fixture.pet_id} actual={resp_dict['id']}"