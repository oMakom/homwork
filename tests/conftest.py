import pytest

@pytest.fixture
def data_operations_dict():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 743628025,
    "state": "EXECUTED",
    "date": "2018-06-04T06:59:55.424356",
    "operationAmount": {
      "amount": "978.31",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "from": "Счет 54883981902864782073",
    "to": "Счет 61834060137088759145"
  },
  {
    "id": 743278119,
    "state": "EXECUTED",
    "date": "2018-10-15T08:05:34.061711",
    "operationAmount": {
      "amount": "51203.12",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "",
    "from": "MasterCard 1435442169918409",
    "to": "Maestro 7452400219469235"
  },]