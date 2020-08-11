import json


def get_robberies(filename='грабители.csv'):
    """
    :return: [{}, {}, {}, {}]
    """
    robberies = []
    file = open(filename, encoding='utf-8')
    file.readline()
    for line in file:
        robbery_list = line.rstrip().split(', ')
        robbery_dict = {
            'имя': robbery_list[0],
            'город': robbery_list[1],
            'жертва': robbery_list[2],
            'украл': transform_theft_thing_from_str_to_dict(robbery_list[3]),
            'дата': robbery_list[4],
            'пойман': robbery_list[5] == 'T',
            'речь': robbery_list[6],
        }
        robberies.append(robbery_dict)

    return robberies


def transform_theft_thing_from_str_to_dict(theft_str):
    """
    'помідор#10; ручка; яблуко#4' -> {'помідор': 10, 'ручка': 1, 'яблуко': 4}

    :param theft_str: речі, які викрав грабіжник
    :return: dict - Ключі: речі. Значення: кількості
    """
    things = theft_str.split('; ')  # ['помідор#10', 'ручка', 'яблуко#4']
    things_dict = {}
    for thing in things:
        if '#' in thing:  # 'помідор#10'
            thing, count_str = thing.split('#')
            things_dict[thing] = int(count_str)
        else:
            things_dict[thing] = 1
    return things_dict


def print_vory():
    print(json.dumps(get_robberies(), indent=4, ensure_ascii=False))


def find_vor_5_1():
    robberies = get_robberies()
    counter_dict = {}
    for robbery in robberies:
        name = robbery['имя']
        success = not robbery['пойман']
        if name not in counter_dict:
            counter_dict[name] = {'удачі': 0, "невдачі": 0}
        if success:
            counter_dict[name]['удачі'] += 1
        else:
            counter_dict[name]['невдачі'] += 1

    names = []
    for vor_name in counter_dict:
        if counter_dict[vor_name]['удачі'] == 5 and counter_dict[vor_name]['невдачі'] == 1:
            names.append(vor_name)

    if len(names) == 1:
        name = names[0]
        for robbery in robberies:
            if robbery['имя'] == name and robbery['пойман'] == True:
                print(robbery['речь'])


def find_konetolub():
    robberies = get_robberies()
    names_counts = {}
    for robbery in robberies:
        things = robbery['украл']
        if 'конфета' in things:
            count = things['конфета']
            name = robbery['имя']
            if name in names_counts:
                names_counts[name] += count
            else:
                names_counts[name] = count

    max_names = []
    max_count = 0
    for name in names_counts:
        if names_counts[name] > max_count:
            max_count = names_counts[name]
            max_names.clear()
            max_names.append(name)
        elif names_counts[name] == max_count:
            max_names.append(name)

    print(names_counts)
    print(max_names)
    print(max_count)


find_konetolub()
