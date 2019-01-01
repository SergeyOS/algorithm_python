# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
in_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив：{in_array}')

if len(in_array) >= 2:
    # Инициализация счетчиков
    first_min = None
    second_min = None
    first_min_index = None
    second_min_index = None

    for index, item in enumerate(in_array):
        if (first_min is None) or (item < first_min):
            second_min = first_min
            second_min_index = first_min_index
            first_min = item
            first_min_index = index
        elif (second_min is None) or (item < second_min):
            second_min = item
            second_min_index = index
    print(f'Два наименьших числа:{first_min}:{first_min_index} и {second_min}:{second_min_index}')
else:
    print('Массив не соответствует задачи')
