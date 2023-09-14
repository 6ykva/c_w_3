import json


def json_load(file_json):
    """
    Загружаем json файл
    """
    with open(file_json, "r", encoding="utf-8") as cat_file:
        data = json.load(cat_file)
        return data


def list_sort(data):
    """
    Сортировка списка словарей по дате,
    создание списка из последних 5 записей
    :param data: Список словарей
    :return: Последние 5 записей с удачными операциями
    """
    operations = []

    for item in data:
        if len(item) != 0 and item['state'] == 'EXECUTED':   #Сортирока по значению EXECUTED
            operations.append(item['date'])
    operations.sort(reverse=True)
    first_five_sort_date = operations[:5]

    first_five_operations = []

    for item in first_five_sort_date:
        for element in data:
            if len(element) > 0:
                if item is element['date']:
                    first_five_operations.append(element)

    return first_five_operations


def mask_from_message(message):
    """
    Функция обработки номера счета и карты
    :param message: Счет карты
    :return: Обработаное значение
    """
    if message is None:
        return ''
    message_split = message.split(' ')
    if message_split[0] == 'Счет':
        secret_number = mask_build_number(message_split[-1])
    else:
        secret_number = mask_card_number(message_split[-1])

    return ' '.join(message_split[:-1]) + ' ' + secret_number


def mask_card_number(number):
    """
    Функция обработки номера счета, если входящее
    значение номер карты то маскируем его номер звездочками
    :param number: номер счета карты
    :return: замаскированный номер счета карты
    """
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]


def mask_build_number(number):
    """
    Функция обработки номера счета, если входящее
    значение номер счета то маскируем его номер звездочками
    :param number: номер счета
    :return: замаскированный номер счета
    """
    if number.isdigit() and len(number) >= 4:
        return '**' + number[-4:]


def final_inf(new_list):
    """
    Функция вывода конечного списка последних 5 отсортированных по дате операций
    :param new_list: список последних 5 удачных операций
    :return: Список последних 5 отсортированных по дате операций
    """
    final_list = []
    for i in new_list:
        check_to = f'Счет **{i["to"][-4:]}'
        date = f'{i["date"][8:10]}.{i["date"][5:7]}.{i["date"][:4]}'
        name = i['operationAmount']['currency']['name']
        amount = i['operationAmount']['amount']
        description = i['description']
        from_number = mask_from_message(i.get('from'))

        if i['description'] == 'Открытие вклада':
            final_list.append(f'{date} {description}\n'
                              f'{check_to}\n{amount} {name}\n')
        else:
            final_list.append(f"{date} {i['description']}\n"
                              f"{from_number} -> {check_to}\n{amount} {name}\n")

    return final_list
