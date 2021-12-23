import pytest

@pytest.mark.parametrize("id", [580, 591])
def test_positive(base_fixture, id):
    token = base_fixture.token
    response = base_fixture.api_surveys.get_survey_by_id(token, id)
    resp_dict = response.json()

    check_resp = base_fixture.checkers.validate_json(resp_dict, "get_survey_by_id.json")
    assert check_resp is True, "тело ответа не соответствует схеме json"

    assert response.status_code == 200, "код ответа не соответствует заданному"

    check_resp_body = base_fixture.checkers.check_get_survey_by_id(id, resp_dict)

    assert check_resp_body is True, f"id не соответствует ожидаемому exp={id} actual={resp_dict['id']}"
