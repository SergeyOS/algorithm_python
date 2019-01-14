# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
import random
import cProfile

SIZE = 1000000
MIN_ITEM = 0
MAX_ITEM = 1000


def init_array(size: int):
    return [random.randint(MIN_ITEM, MAX_ITEM * size) for _ in range(size)]


# 1. Алгоритм с рекурсией

def count_rec(size: int):
    enter_numbers = init_array(size)  # имитация ввода чисел
    enter_element = random.randint(0, 9)  # имитация ввода цифры

    # print(f'Исходный массив：{enter_numbers}. Считаем {enter_element}')
    def count_in_value(value: int, element: int) -> int:
        i = 0
        if value % 10 == element:
            i = 1

        if value // 10 == 0:
            return i
        else:
            return i + count_in_value(value // 10, element)

    result_count = 0
    for i in range(len(enter_numbers)):
        result_count += count_in_value(enter_numbers[i], enter_element)

    return result_count


# 100 loops, best of 5: 253 usec per loop -     100
# 100 loops, best of 5: 2.87 msec per loop -   1000
# 100 loops, best of 5: 31.8 msec per loop -  10000
# 100 loops, best of 5: 341 msec per loop -  100000
# 100 loops, best of 5: 3.76 sec per loop - 1000000
# cProfile.run('count_rec(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.505    0.505 <string>:1(<module>)
#    100001    0.066    0.000    0.143    0.000 random.py:174(randrange)
#    100001    0.029    0.000    0.172    0.000 random.py:218(randint)
#    100001    0.052    0.000    0.077    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.202    0.202 task3.py:11(init_array)
#         1    0.030    0.030    0.202    0.202 task3.py:12(<listcomp>)
#         1    0.027    0.027    0.503    0.503 task3.py:17(count_rec)
# 788844/100000    0.274    0.000    0.274    0.000 task3.py:22(count_in_value) # Рекурсивный вызов
#         1    0.001    0.001    0.506    0.506 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100001    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    134563    0.018    0.000    0.018    0.000 {method 'getrandbits' of '_random.Random' objects}


# 1. Алгоритм с циклом

def count_loop(size: int):
    enter_numbers = init_array(size)  # имитация ввода чисел
    enter_element = random.randint(0, 9)  # имитация ввода цифры
    # print(f'Исходный массив：{enter_numbers}. Считаем {enter_element}')
    result_count = 0
    for i in range(len(enter_numbers)):
        value = enter_numbers[i]
        while value // 10 != 0:
            if value % 10 == enter_element:
                result_count += 1
            value = value // 10

    return result_count
# 100 loops, best of 5: 190 usec per loop  -     100
# 100 loops, best of 5: 2.04 msec per loop -    1000
# 100 loops, best of 5: 23.3 msec per loop -   10000
# 100 loops, best of 5: 249 msec per loop  -  100000
# 100 loops, best of 5: 2.65 sec per loop  - 1000000
# cProfile.run('count_loop(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.002    0.002    0.325    0.325 <string>:1(<module>)
# 100001    0.068    0.000    0.145    0.000 random.py:174(randrange)
# 100001    0.030    0.000    0.175    0.000 random.py:218(randint)
# 100001    0.052    0.000    0.077    0.000 random.py:224(_randbelow)
#      1    0.000    0.000    0.208    0.208 task3.py:11(init_array)
#      1    0.033    0.033    0.208    0.208 task3.py:12(<listcomp>)
#      1    0.115    0.115    0.323    0.323 task3.py:60(count_for)
#      1    0.001    0.001    0.326    0.326 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100001    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 134544    0.018    0.000    0.018    0.000 {method 'getrandbits' of '_random.Random' objects}


# Вывод:
# Алгоритм с рекурсией более медленный и забивает стек. При этом средняя скорость и алгоритма с рекурсией
# и с алгоритма с циклом  прямо пропорциональна размеру массива.

# print(count_rec(100000))
# print(count_loop(100000))
