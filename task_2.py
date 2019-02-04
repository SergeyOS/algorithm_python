# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random
import operator

ARRAY_SIZE = 10
LEFT_VALUE = 0
RIGHT_VALUE = 50
DEBUG = False
REVERSE = False


def get_operator(reverse):
    if reverse:
        return operator.lt
    else:
        return operator.gt


def merge_sort(source_array, reverse=False):
    # массив уже отсортирован
    if len(source_array) <= 1:
        return source_array
    op = get_operator(reverse)  # выбор направление сортировки
    # Сортируемый массив разбивается на две части примерно одинакового размера;
    middle_idx = len(source_array) // 2
    # Каждая из получившихся частей сортируется отдельно
    left_array = merge_sort(source_array[0:middle_idx], reverse)
    right_array = merge_sort(source_array[middle_idx:len(source_array)], reverse)

    # Два упорядоченных массива соединяются в один
    left_idx = 0
    right_idx = 0
    target = []
    while left_idx < len(left_array) and right_idx < len(right_array):
        if op(left_array[left_idx], right_array[right_idx]):
            target.append(right_array[right_idx])
            right_idx += 1
        else:
            target.append(left_array[left_idx])
            left_idx += 1

    # Сливаем хвосты
    while left_idx < len(left_array):
        target.append(left_array[left_idx])
        left_idx += 1
    while right_idx < len(right_array):
        target.append(right_array[right_idx])
        right_idx += 1

    return target


def init_array(enter_size=ARRAY_SIZE):
    # array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7, -1]
    array = [LEFT_VALUE + (RIGHT_VALUE - LEFT_VALUE) * random.random() for _ in range(enter_size)]
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
    result_array = merge_sort(source_array.copy(), reverse=REVERSE)
    print(f'Итоговый массив {result_array}')
    unit_test(source_array, result_array, reverse=REVERSE)

else:
    print(f'Итоговый массив {merge_sort(init_array(), reverse=REVERSE)}')
