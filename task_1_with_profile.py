# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Для анализа взята задача из Урока 3 со следующим условием
# 4. Определить, какое число в массиве встречается чаще всего.

import random
from memory_profiler import profile
from collections import defaultdict

SIZE = 1000
MIN_ITEM = -1000
MAX_ITEM = 1000


@profile(precision=5)
def function_version1():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     19  16.11719 MiB  16.11719 MiB   @profile(precision=5)
#     20                             def function_version1():
#     21  16.12109 MiB   0.00391 MiB       array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     22  16.12109 MiB   0.00000 MiB       print(f'Исходный массив：{array}')
#     23
#     24                                 # формируем словарь с частотой чисел
#     25  16.12109 MiB   0.00000 MiB       out_dict = dict()
#     26  16.16016 MiB   0.00000 MiB       for item in array:
#     27  16.16016 MiB   0.00000 MiB           if out_dict.get(item) is not None:
#     28  16.16016 MiB   0.00000 MiB               out_dict[item] += 1
#     29                                     else:
#     30  16.16016 MiB   0.03906 MiB               out_dict[item] = 1
#     31
#     32                                 # формируем множество с выборкой чаще всего встречающихся чисел
#     33  16.16016 MiB   0.00000 MiB       out_set = set()
#     34  16.16016 MiB   0.00000 MiB       max_count = 0
#     35  16.16016 MiB   0.00000 MiB       for key, item in out_dict.items():
#     36  16.16016 MiB   0.00000 MiB           if item > max_count:
#     37  16.16016 MiB   0.00000 MiB               out_set = {key, }
#     38  16.16016 MiB   0.00000 MiB               max_count = item
#     39  16.16016 MiB   0.00000 MiB           elif item == max_count:
#     40  16.16016 MiB   0.00000 MiB               out_set.add(key)
#     41  16.16406 MiB   0.00391 MiB       print(f'Следующие числа встречаются чаще всего:{out_set} - {max_count} раз')


@profile(precision=5)
def function_version2():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     69  16.09766 MiB  16.09766 MiB   @profile(precision=5)
#     70                             def function_version2():
#     71  16.10156 MiB   0.00391 MiB       array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     72  16.12109 MiB   0.01953 MiB       print(f'Исходный массив：{array}')
#     73  16.12109 MiB   0.00000 MiB       counter = {}
#     74  16.12109 MiB   0.00000 MiB       frequency = 1
#     75  16.12109 MiB   0.00000 MiB       out_set = set()
#     76  16.16406 MiB   0.00000 MiB       for item in array:
#     77  16.16406 MiB   0.00000 MiB           if item in counter:
#     78  16.16406 MiB   0.00000 MiB               counter[item] += 1
#     79                                     else:
#     80  16.16406 MiB   0.03516 MiB               counter[item] = 1
#     81  16.16406 MiB   0.00000 MiB           if counter[item] > frequency:
#     82  16.12109 MiB   0.00000 MiB               frequency = counter[item]
#     83  16.12109 MiB   0.00000 MiB               out_set = {item, }
#     84  16.16406 MiB   0.00000 MiB           elif counter[item] == frequency:
#     85  16.16406 MiB   0.00000 MiB               out_set.add(item)
#     86
#     87  16.16797 MiB   0.00391 MiB       print(f'Число {out_set} встречется {frequency} раз(а)')


@profile(precision=5)
def function_version3():
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
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


# Line #    Mem usage    Increment   Line Contents
# ================================================
#    112  16.08984 MiB  16.08984 MiB   @profile(precision=5)
#    113                             def function_version3():
#    114  16.09375 MiB   0.00391 MiB       array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#    115  16.09375 MiB   0.00000 MiB       print(f'Исходный массив：{array}')
#    116  16.09375 MiB   0.00000 MiB       out_set = set()
#    117  16.09375 MiB   0.00000 MiB       out_set.add(array[0])
#    118  16.09375 MiB   0.00000 MiB       frequency = 1
#    119  16.12891 MiB   0.00000 MiB       for i in range(len(array)):
#    120  16.12891 MiB   0.00000 MiB           spam = 1
#    121  16.12891 MiB   0.00781 MiB           for j in range(i + 1, len(array)):
#    122  16.12891 MiB   0.00781 MiB               if array[i] == array[j]:
#    123  16.12891 MiB   0.00000 MiB                   spam += 1
#    124  16.12891 MiB   0.00000 MiB           if spam > frequency:
#    125  16.09375 MiB   0.00000 MiB               frequency = spam
#    126  16.09375 MiB   0.00000 MiB               out_set.clear()
#    127  16.09375 MiB   0.00000 MiB               out_set.add(array[i])
#    128  16.12891 MiB   0.00000 MiB           elif spam == frequency:
#    129  16.09375 MiB   0.00000 MiB               out_set.add(array[i])
#    130
#    131  16.13281 MiB   0.00391 MiB       print(f'Число {out_set} встречется {frequency} раз(а)')

# Вывод: есть незначительная зависимость от random
# Наименьший объем памяти использует function_version3, но данный алгоритм крайне медленный
# Версия Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
# ОС: Windows 10 x64

if __name__ == "__main__":
    enter_key = (input('введите вариант (1,2,3):'))
    selector = defaultdict(lambda: None, {'1': function_version1, '2': function_version2, '3': function_version3})
    selector[enter_key]()
