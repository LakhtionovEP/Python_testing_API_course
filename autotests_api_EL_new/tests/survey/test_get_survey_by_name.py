import pytest

@pytest.mark.parametrize("subs", ["EL"])
def test_positive(base_fixture, subs):
    token = base_fixture.token
    response = base_fixture.api_surveys.get_survey_by_subs(token, subs)
    resp_dict = response.json()

    check_resp = base_fixture.checkers.validate_json(resp_dict, "get_survey_by_name_full.json")
    assert check_resp is True, "тело ответа не соответствует схеме json"

    check_resp = base_fixture.checkers.validate_items(resp_dict, "get_survey_by_name.json")
    assert check_resp is True, f"следующие id не соответствует схеме json{tuple(check_resp.keys())}"

    assert response.status_code == 200, "код ответа не соответствует заданному"
