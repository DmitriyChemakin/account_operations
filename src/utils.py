import json
from datetime import datetime


def loading_file(file_name):
    """Функция принимает файл с данными"""
    with open(file_name, 'r', encoding='utf-8') as load_file:
        return json.load(load_file)


def filter_list(load_file):
    """Функция фильтрует все данные из переданного в неё файла"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective


# a = check_list(loading_file('operations.json'))

def sorts_date(json_adjective):
    """Функция преобразует и возвращает дату и время в нужном формате"""
    json_sort = sorted(json_adjective, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort

# print(sorts_date(filter_list(loading_file('operations.json'))))


def get_date(date):
    """Возвращает дату в нужном формате"""
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


# print(get_date('2019-12-08T22:46:21.935582'))

def get_hide_number(num):
    """Функция преобразует и возвращает номер карты и счета в нужном формате"""
    tmp = num.split()  # Разделение строки по пробелам
    if tmp[0] == 'Счет':
        # Формирование скрытого номера счета
        return 'Счет **' + num[-4:]
    else:
        card_name = ' '.join(tmp[:-1])  # Формирование названия карты
        # Формирование скрытого номера карты
        return card_name + ' ' + tmp[-1][:4] + ' ' + tmp[-1][4:6] + '** **** ' + tmp[-1][-4:]

# print(get_hide_number("Visa Platinum 2241653116508487"))


def get_money(cash):
    """Функция возвращает сумму и валюту"""
    return f'{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}'


def get_main(num_operation=5):
    load_json = loading_file('operations.json')
    fil = filter_list(load_json)
    sort = sorts_date(fil)
    for operation in sort:
        if num_operation == 0:
            break

        print(get_date(operation["date"]), operation["description"])

        if operation["description"] != "Открытие вклада":
            print(get_hide_number(operation["from"]) + " -> ", end='')

        print(get_hide_number(operation["to"]))
        print(get_money(operation), "\n")
        num_operation -= 1




















