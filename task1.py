# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
in_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
out_array = []

for index, item in enumerate(in_array):
    if item % 2 == 0:
        out_array.append(index)
print(f'Исходный массив：{in_array}')
print(f'Массив с индексами четных чисел исходного массива：{out_array}')
