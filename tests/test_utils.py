import os
from config import ROOT_DIR
from src.utils import loading_file, filter_list, sorts_date_time, get_date, get_hide_number, get_money, get_main


def test_loading_file():
    TEST_DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert loading_file(TEST_DATA_PATH) == [1, 2, 3, 4, 5]


test_executed = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041"
    },
    {},
    {
        "id": 441945887,
        "state": "EXECUTED",
        "date": "2019-10-26T10:50:58.294042"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689"
    }
]


def test_filter_list():
    assert filter_list(test_executed) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "id": 441945887,
            "state": "EXECUTED",
            "date": "2019-10-26T10:50:58.294042"
        }
    ]


test_date_time = [
    {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
    },
    {
        "id": 518707726,
        "state": "EXECUTED",
        "date": "2018-11-29T07:18:23.941293"
    }
]


def test_sorts_date_time():
    assert sorts_date_time(test_date_time) == [
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293"
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
        }
    ]


test_date = "2018-04-14T19:35:28.978265"


def test_get_date():
    assert get_date(test_date) == "14.04.2018"


def test_get_hide_number():
    assert get_hide_number("Visa Gold 9447344650495960") == 'Visa Gold 9447 34** **** 5960'
    assert get_hide_number("Счет 97584898735659638967") == "Счет **8967"
    assert get_hide_number("Visa Gold 9447344650495960") == 'Visa Gold 9447 34** **** 5960'
    assert get_hide_number("Visa Gold 9447344650495960") == "Visa Gold 9447 34** **** 5960"


def test_get_money():
    assert get_money({
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    }) == '48223.05 руб.'


def test_get_main():
    pass
