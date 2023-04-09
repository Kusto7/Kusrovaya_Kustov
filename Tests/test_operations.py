from main.utils import sorted_data, mask_card, formatted_data, load_data


def test_sorted_data():
    data1 = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2019-11-13T17:38:04.800051'
        },
        {
            'id': 2,
            'state': 'CANCELED',
            'date': '2019-06-30T15:11:53.136004'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2019-04-19T12:02:30.129240'
        }
    ]
    data2 = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2019-11-13T17:38:04.800051'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2019-04-19T12:02:30.129240'
        }
    ]
    assert sorted_data(data1) == data2


def test_mask_card():
    card1 = 'Visa Platinum 1813166339376336'
    card2 = 'Счет 33355011456314142963'
    assert mask_card(card1) == 'Visa Platinum 1813 16** **** 6336'
    assert mask_card(card2) == 'Счет **2963'


def test_formatted_data():
    data1 = {
    "id": 879660146,
    "state": "EXECUTED",
    "date": "2018-07-22T07:42:32.953324",
    "operationAmount": {
      "amount": "92130.50",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 19628854383215954147",
    "to": "Счет 90887717138446397473"
  }
    data2 = {
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  }
    assert formatted_data(data1) == "22.07.2018 Перевод организации\n" \
                                    "Счет **4147 -> Счет **7473\n" \
                                    "92130.50 USD\n"
    assert formatted_data(data2) == "03.02.2018 Открытие вклада\n" \
                                    "Счет **8767\n" \
                                    "90297.21 руб.\n"


def test_load_data():
    data1 = [{
    "id": 902831954,
    "state": "EXECUTED",
    "date": "2018-04-22T17:01:46.885252",
    "operationAmount": {
      "amount": "84732.61",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 3530191547567121",
    "to": "Счет 46878338893256147528"
  }]
    assert load_data('test.json') == data1
