# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках

import random

DEBUG = False
LEFT_VALUE = 0
RIGHT_VALUE = 100
M = 5


def quick_select(spam_array: list, index_mediana: int):
    if len(spam_array) == 1:
        return spam_array[0]

    spam = random.choice(spam_array)

    left = []
    center = []
    right = []

    for item in spam_array:
        if item < spam:
            left.append(item)
        elif item == spam:
            center.append(item)
        else:
            right.append(item)
    if index_mediana < len(left):
        return quick_select(left, index_mediana)
    elif index_mediana < len(left) + len(center):
        return spam
    else:
        return quick_select(right, index_mediana - len(left) - len(center))


def init_array():
    # array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7, -1]
    array = [random.randrange(LEFT_VALUE, RIGHT_VALUE) for _ in range(2 * M + 1)]
    print(f'Исходный масив:{array}')
    return array


def unit_test(source_array: list, mediana):
    spam_array = sorted(source_array)
    print(f'Отсортированный массив:{spam_array}')
    med = len(spam_array) // 2
    assert spam_array[med] == mediana
    print(f'Test mediana OK')


if DEBUG:
    source_array = init_array()
    result_array = source_array.copy()
    mediana = quick_select(result_array, M)
    print(f'Медиана равна {mediana}')
    unit_test(source_array, mediana)
else:
    result_array = init_array()
    mediana = quick_select(result_array, M)
    print(f'Медиана равна {mediana}')
    print(f'Отсортированный массив:{sorted(result_array)}')
