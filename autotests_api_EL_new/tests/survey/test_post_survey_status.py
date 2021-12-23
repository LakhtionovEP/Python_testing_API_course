import pytest

#ACTIVE/DISABLED/DRAFT/DELETED
@pytest.mark.parametrize("id, status", [(594, "ACTIVE")])
def test_positive(base_fixture, id, status):
    token = base_fixture.token
    response = base_fixture.api_surveys.post_survey_status(token, id, status)
    resp_dict = response.json()
    print(resp_dict)
    check_resp = base_fixture.checkers.validate_json(resp_dict, "post_survey_status.json")
    assert check_resp is True, "тело ответа не соответствует схеме json"

    assert response.status_code == 200, "код ответа не соответствует заданному"

    check_resp_body = base_fixture.checkers.check_post_survey_status(resp_dict)
    assert check_resp_body is True, "изменение статуса опроса провалено"