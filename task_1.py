# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
import operator

ARRAY_SIZE = 10
LEFT_VALUE = -100
RIGHT_VALUE = 100
DEBUG = False
REVERSE = True


def get_operator(reverse):
    if reverse:
        return operator.lt
    else:
        return operator.gt


def bubble_sort(array, reverse=False):
    op = get_operator(reverse)  # выбор направление сортировки
    n = 1
    while n < len(array):
        for i in range(len(array) - n):  # оптимизация
            if op(array[i], array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


def init_array(enter_size=ARRAY_SIZE):
    # array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7, -1]
    array = [random.randrange(LEFT_VALUE, RIGHT_VALUE) for _ in range(enter_size)]  # [LEFT_VALUE; RIGHT_VALUE)
    print(f'Исходный масив:{array}')
    return array


def unit_test(source_array, result_array, reverse=False):
    if len(source_array) == len(result_array):
        print(f'Test len OK')
        spam_array = sorted(source_array, reverse=reverse)
        for i in range(len(source_array)):
            assert spam_array[i] == result_array[i]
            print(f'Test {i} OK')
    else:
        print(f'Test len BAD')


if DEBUG:
    source_array = init_array()
    result_array = source_array.copy()
    bubble_sort(result_array, REVERSE)
    print(f'Итоговый массив {result_array}')
    unit_test(source_array, result_array, REVERSE)

else:
    result_array = init_array()
    bubble_sort(result_array, reverse=REVERSE)
    print(f'Итоговый массив {result_array}')
