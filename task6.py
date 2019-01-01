# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

ROW_SIZE = 5
COLUMN_SIZE = 7
MIN_ITEM = -100
MAX_ITEM = 100
in_matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMN_SIZE)] for _ in range(ROW_SIZE)]

min_items = [MAX_ITEM] * len(in_matrix[0])
for line in in_matrix:

    for i, item in enumerate(line):
        print(f'{item:>4}', end=' \t')
        if min_items[i] > item:
            min_items[i] = item
    print('')

print(f'Минимальных элементы столбцов матрицы {min_items}')

max_item = min_items[0]
for item in min_items:
    if max_item < item:
        max_item = item
print(f'максимальный элемент среди минимальных элементов столбцов матрицы {max_item}')
