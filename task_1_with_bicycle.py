# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Для анализа взята задача из Урока 3 со следующим условием
# 4. Определить, какое число в массиве встречается чаще всего.

import random
import sys
from collections import defaultdict

SIZE_ARRAY = 1000
MIN_ITEM = -1000
MAX_ITEM = 1000

dict_variable = dict()


def size_of_object(x):
    size_object = sys.getsizeof(x)
    if isinstance(x, (list, dict, tuple, set)):  # нужно добавить все сложные структуры
        # hasattr(x, '__iter__') # изменяет исходные структуры. Причину не нашел.
        if not isinstance(x, str):
            for item in x:
                size_object += size_of_object(item)
    return size_object


def traceit(frame, event, arg):
    if event == "line":
        for key in frame.f_locals.keys():
            size_object = size_of_object(frame.f_locals[key])

            if (dict_variable.get(key) is None) or (dict_variable[key] < size_object):
                dict_variable[key] = size_object

    return traceit


def function_version1():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARRAY)]
    print(f'Исходный массив：{array}')
    # формируем словарь с частотой чисел
    out_dict = dict()
    for item in array:
        if out_dict.get(item) is not None:
            out_dict[item] += 1
        else:
            out_dict[item] = 1

    # формируем множество с выборкой чаще всего встречающихся чисел
    out_set = set()
    max_count = 0
    for key, item in out_dict.items():
        if item > max_count:
            out_set = {key, }
            max_count = item
        elif item == max_count:
            out_set.add(key)
    print(f'Следующие числа встречаются чаще всего:{out_set} - {max_count} раз')


# *********************function_version1****************************************************
# Переменные в функции использует следующие объемы памяти:
# Переменная ".0":32
# Переменная "self":2560
# Переменная "a":28
# Переменная "b":28
# Переменная "start":28
# Переменная "stop":28
# Переменная "step":28
# Переменная "_int":400
# Переменная "istart":28
# Переменная "istop":28
# Переменная "width":28
# Переменная "n":28
# Переменная "int":400
# Переменная "maxsize":32
# Переменная "type":400
# Переменная "Method":400
# Переменная "BuiltinMethod":400
# Переменная "random":72
# Переменная "getrandbits":72
# Переменная "k":28
# Переменная "r":28
# Переменная "_":28
# Переменная "array":37020
# Переменная "out_dict":59000
# Переменная "item":28
# Переменная "out_set":932
# Переменная "max_count":28
# Переменная "key":28
# Общий объем памяти 102140
#
def function_version2():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARRAY)]
    print(f'Исходный массив：{array}')
    counter = {}
    frequency = 1
    out_set = set()
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            out_set = {item, }
        elif counter[item] == frequency:
            out_set.add(item)

    print(f'Число {out_set} встречется {frequency} раз(а)')


# ********************function_version2******************************************************
# Переменные в функции использует следующие объемы памяти:
# Переменная ".0":32
# Переменная "self":2560
# Переменная "a":28
# Переменная "b":28
# Переменная "start":28
# Переменная "stop":28
# Переменная "step":28
# Переменная "_int":400
# Переменная "istart":28
# Переменная "istop":28
# Переменная "width":28
# Переменная "n":28
# Переменная "int":400
# Переменная "maxsize":32
# Переменная "type":400
# Переменная "Method":400
# Переменная "BuiltinMethod":400
# Переменная "random":72
# Переменная "getrandbits":72
# Переменная "k":28
# Переменная "r":28
# Переменная "_":28
# Переменная "array":37020
# Переменная "counter":59756
# Переменная "frequency":28
# Переменная "out_set":3448
# Переменная "item":28
# Общий объем памяти 105384


def function_version3():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARRAY)]
    print(f'Исходный массив：{array}')
    out_set = set()
    out_set.add(array[0])
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            out_set.clear()
            out_set.add(array[i])
        elif spam == frequency:
            out_set.add(array[i])

    print(f'Число {out_set} встречется {frequency} раз(а)')


# *****************function_version3**************************************************************
# Переменные в функции использует следующие объемы памяти:
# Переменная ".0":32
# Переменная "self":2560
# Переменная "a":28
# Переменная "b":28
# Переменная "start":28
# Переменная "stop":28
# Переменная "step":28
# Переменная "_int":400
# Переменная "istart":28
# Переменная "istop":28
# Переменная "width":28
# Переменная "n":28
# Переменная "int":400
# Переменная "maxsize":32
# Переменная "type":400
# Переменная "Method":400
# Переменная "BuiltinMethod":400
# Переменная "random":72
# Переменная "getrandbits":72
# Переменная "k":28
# Переменная "r":28
# Переменная "_":28
# Переменная "array":37024
# Переменная "out_set":988
# Переменная "frequency":28
# Переменная "i":28
# Переменная "spam":28
# Переменная "j":28
# Общий объем памяти 43228

# Вывод: есть незначительная зависимость от random
# Наименьший объем памяти использует function_version3, но данный алгоритм крайне медленный
# Версия Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
# ОС: Windows 10 x64


if __name__ == "__main__":
    enter_key = (input('введите вариант (1,2,3):'))
    selector = defaultdict(lambda: None, {'1': function_version1, '2': function_version2, '3': function_version3})
    sys.settrace(traceit)
    try:
        selector[enter_key]()
        print('*' * 100)
        print(f'Переменные в функции использует следующие объемы памяти:')
        total = 0
        for key in dict_variable:
            print(f'Переменная "{key}":{dict_variable[key]}')
            total += dict_variable[key]
        print(f'Общий объем памяти {total}')
    finally:
        sys.settrace(None)
