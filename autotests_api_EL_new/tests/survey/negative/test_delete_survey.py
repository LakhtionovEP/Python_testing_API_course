import pytest

@pytest.mark.parametrize("id", [597])
def test_negative(base_fixture, id):
    token = base_fixture.token
    response = base_fixture.api_surveys.delete_survey_by_id(token, id)
    resp_dict = response.json()

    #check_resp = base_fixture.checkers.validate_json(resp_dict, "get_survey_by_id.json")
    #assert check_resp is True, "тело ответа не соответствует схеме json"

    assert response.status_code == 500, "код ответа не соответствует заданному"

