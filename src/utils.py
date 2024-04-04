import json
from datetime import datetime


def loading_file(file_name):
    """Функция принимает файл с данными"""
    with open(file_name, 'r', encoding='utf-8') as load_file:
        return json.load(load_file)


def filter_list(load_file):
    """Функция фильтрует (сортирует) все данные из переданного в неё файла"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective




def sorts_date_time(json_adjective):
    """Функция преобразует и возвращает дату и время в нужном формате"""
    json_sort = sorted(json_adjective, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort




def get_date(date):
    """Возвращает дату в нужном формате"""
    obj_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(obj_date, '%d.%m.%Y')




def get_hide_number(num):
    """Функция преобразует и возвращает номер карты и счета в нужном скрытом формате"""
    tmp = num.split()
    if tmp[0] == 'Счет':
        return 'Счет **' + num[-4:]
    else:
        card_name = ' '.join(tmp[:-1])
        return card_name + ' ' + tmp[-1][:4] + ' ' + tmp[-1][4:6] + '** **** ' + tmp[-1][-4:]




def get_money(cash):
    """Функция возвращает сумму и валюту"""
    return f'{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}'


def get_main(num_operation=5):
    """Главная функция, принимает результат предыдущих функций и выводит нужный результат"""
    load_json = loading_file('operations.json')
    fil = filter_list(load_json)
    sort = sorts_date_time(fil)
    for operation in sort:
        if num_operation == 0:
            break

        print(get_date(operation["date"]), operation["description"])

        if operation["description"] != "Открытие вклада":
            print(get_hide_number(operation["from"]) + " -> ", end='')

        print(get_hide_number(operation["to"]))
        print(get_money(operation), "\n")
        num_operation -= 1




















