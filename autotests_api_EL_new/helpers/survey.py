import random
words1 = ['тестовый', 'боевой', 'продуктивный', 'стейджовый', 'препродовский', 'дев']
words2 = ['опрос', 'вопрос', 'вариант']


class Helpers:
    @staticmethod
    def survey_gen():
        body = {
  "title": "EL_new_post7",
  "businessTitle": "EL_new_post7",
  "thankPage": {
    "title": "Спасибо, что прошли опрос",
    "description": "",
    "linkEnabled": False,
    "linkText": "",
    "linkUrl": "",
    "utmConfig": {
      "utmSource": "",
      "utmMedium": "",
      "utmCampaign": "",
      "utmContent": "",
      "utmTerm": ""
    }
  },
  "surveyPage": [
    {
      "id": 1012,
      "attributes": None,
      "title": "",
      "visibleIf": None,
      "surveyQuestion": [
        {
          "id": 9000,
          "type": "RADIOGROUP",
          "attributes": {
            "title": f"Это {random.choice(words1)} {random.choice(words2)}",
            "showNumbers": True,
            "hasOther": False,
            "isRequired": True,

            "values": [
              {
                "id": 9000000000,
                "value": f"1 {random.choice(words2)}",
                "withComment": False
              },
              {
                "id": 9000000001,
                "value": f"2 {random.choice(words2)}",
                "withComment": False
              }
            ]

          },
          "visibleIf": None,
          "sequenceId": "abcd",
          "junction": [
            {
              "answers": [
                "string"
              ],
              "sequenceId": "string"
            }
          ]
        }
      ]
    }
  ],
  "categories": [
  ],
  "showQuestionCount": True,
  "complicated": False
}
        return body
