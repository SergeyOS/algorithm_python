# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
in_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив：{in_array}')

# формируем словарь с частотой чисел
out_dict = dict()
for item in in_array:
    if out_dict.get(item) is not None:
        out_dict[item] += 1
    else:
        out_dict[item] = 1
print(f'Частота чисел в исходном словаре：{out_dict}')

# формируем множество с выборкой чаще всего встречающихся чисел
out_set = {}
max_count = 0
for key, item in out_dict.items():
    if item > max_count:
        out_set = {key, }
        max_count = item
    elif item == max_count:
        out_set.add(key)
print(f'Следующие числа встрчаются чаще  всего:{out_set} - {max_count} раз')
