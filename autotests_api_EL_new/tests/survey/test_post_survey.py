import pytest


@pytest.mark.parametrize("title, name, type", [("EL_test_10", "RG_TEST", "RADIOGROUP"), ("EL_test_11", "CH_TEST", "CHECKBOX")])
def test_positive(base_fixture, title, name, type):
    body = base_fixture.helpers.survey_gen()
    body['title'] = title
    body['businessTitle'] = name
    body['surveyPage'][0]['surveyQuestion'][0]['type'] = type
    print(body)
    response = base_fixture.api_surveys.post_survey(body)
    resp_dict = response.json()
    print(resp_dict)
    check_resp = base_fixture.checkers.validate_json(resp_dict, "post_survey.json")
    assert check_resp is True, "тело ответа не соответствует схеме json"

    assert response.status_code == 200, "код ответа не соответствует заданному"

    check_resp_body = base_fixture.checkers.check_post_survey(title, name, type, body)
    assert check_resp_body is True, "созданный опросы не соответствуют переданным значениям"