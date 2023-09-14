from utils.utils import (json_load, list_sort,
                         mask_from_message, mask_card_number,
                         mask_build_number, final_inf)
import pytest


@pytest.fixture
def test_json():
    file = 'oper.json'
    return file


@pytest.fixture
def test_json_file():
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
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-04T18:35:29.512364",
            "operationAmount": {
                "amount": "821.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 11113033484347895560",
            "to": "Счет 35383033474447895560"
        }
    ]


@pytest.fixture
def test_json_element():
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
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-04T18:35:29.512364",
            "operationAmount": {
                "amount": "821.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 11113033484347895560",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        }
    ]


def test_list_sort(test_json_file):
    assert list_sort('') == []
    assert list_sort(test_json_file) == [
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
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-04T18:35:29.512364",
            "operationAmount": {
                "amount": "821.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 11113033484347895560",
            "to": "Счет 35383033474447895560"
        }
    ]


def test_mask_from_message():
    assert mask_from_message(None) == ''
    assert (mask_from_message("Maestro 1596837868705199") ==
            "Maestro 1596 83** **** 5199")


def test_mask_card_number():
    assert mask_card_number('1234567891234567') == '1234 56** **** 4567'
    assert mask_card_number('123456789123456') is None


def test_mask_build_number():
    assert mask_build_number("Maestro 1596837868705199") is None
    assert mask_build_number('1596837868705199') == '**5199'


def test_final_inf(test_json_element):
    assert final_inf(test_json_element) == ["26.08.2019 Перевод организации\nMaestro 1596 "
                                            "83** **** 5199 -> Счет **9589\n31957.58 руб."
                                            "\n", "04.07.2019 Перевод со счета на счет"
                                                  "\nСчет **5560 -> Счет **5560\n821.37 USD\n",
                                            "11.07.2018 Открытие вклада\nСчет **6215\n"
                                            "79931.03 руб.\n"]


def test_json_load(test_json):
    assert json_load(test_json) == [
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
        }]
