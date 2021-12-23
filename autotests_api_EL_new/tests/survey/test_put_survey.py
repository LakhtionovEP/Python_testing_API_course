import pytest

@pytest.mark.parametrize("id, name", [(597, "Updated_new")])
def test_positive(base_fixture, id, name):
    token = base_fixture.token
    response = base_fixture.api_surveys.get_survey_by_id(token, id)
    resp_dict = response.json()
    print(resp_dict)
    resp_dict['businessTitle'] = name

    response = base_fixture.api_surveys.put_survey(token, id, resp_dict)

    assert response.status_code == 200, "код ответа не соответствует заданному"

    check_resp = base_fixture.checkers.validate_json(resp_dict, "post_survey.json")
    assert check_resp is True, "тело ответа не соответствует схеме json"