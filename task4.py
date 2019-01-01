# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
in_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив：{in_array}')

index_min_item = 0
index_max_item = 0
min_item = in_array[index_min_item]
max_item = in_array[index_max_item]

for index, item in enumerate(in_array):
    if item > max_item:
        max_item = item
        index_max_item = index
    if item < min_item:
        min_item = item
        index_min_item = index

sum_items = 0
left_index = 0
right_index = 0
if index_max_item > index_min_item:
    left_index = index_min_item
    right_index = index_max_item
else:
    left_index = index_max_item
    right_index = index_min_item

# print(f'Суммируем массив:{in_array[left_index+1:right_index]}')
for index, item in enumerate(in_array):
    if (index > left_index) and (index < right_index):
        sum_items += item
    elif index >= right_index:
        break
print(f'Сумма между минимальным {min_item} и максимальным элементами {max_item} равна {sum_items}')
