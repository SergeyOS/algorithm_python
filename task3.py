# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
in_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив：{in_array}')

max_negative = MIN_ITEM
set_index_max_negative = {}
for index, item in enumerate(in_array):
    if (item < 0) and (max_negative < item):
        max_negative = item
        set_index_max_negative = {index, }
    elif item == max_negative:
        set_index_max_negative.add(index)

if len(set_index_max_negative) == 0:
    print('Отрицательные числа не найдены')
else:
    print(f'Максимальное отрицательное значение {max_negative} расположено :{set_index_max_negative}')
