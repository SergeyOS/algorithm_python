#  2. Написать два алгоритма нахождения i-го по счёту простого числа.
#  Без использования «Решета Эратосфена»;
#  Используя алгоритм «Решето Эратосфена»
import cProfile

MAX_LIMIT_NUMBER = 1000000
KOEFF_ARRAY = 1000 # костыль, решающий проблему с ограничением массива


# 1. Используя алгоритм «Решето Эратосфена»
def sieve(num):
    if num <= 0:
        return -1
    elif num >= MAX_LIMIT_NUMBER:
        return -1
    size = num * KOEFF_ARRAY
    spam_list = [True] * size
    spam_list[0] = False
    spam_list[1] = False
    m = 2
    num_simple_number = 0
    while m < size:
        if spam_list[m]:
            j = m * 2
            num_simple_number += 1
            if num == num_simple_number:
                return m
            while j < size:
                spam_list[j] = False
                j = j + m
        m += 1
    else:
        return -1


# 100 loops, best of 5: 1.46 msec per loop -  10
# 100 loops, best of 5: 21 msec per loop   - 100
# 100 loops, best of 5: 131 msec per loop  -  500
# 100 loops, best of 5: 293 msec per loop - 1000
# 100 loops, best of 5: 3.36 sec per loop - 9999
# cProfile.run('sieve(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.281    0.281 <string>:1(<module>)
#         1    0.278    0.278    0.278    0.278 task2.py:11(sieve)
#         1    0.000    0.000    0.281    0.281 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2.  Без использования «Решета Эратосфена»;
def no_sieve(num):
    if num <= 0:
        return -1
    elif num >= MAX_LIMIT_NUMBER:
        return -1
    size = num * KOEFF_ARRAY
    num_simple_number = 0
    for spam in range(2, size):
        eggs = 2
        while eggs * eggs <= spam:
            if spam % eggs == 0:
                break
            eggs += 1
        else:
            num_simple_number += 1
            if num == num_simple_number:
                return spam
    return -1


# 100 loops, best of 5: 6.4 usec per loop - 10
# 100 loops, best of 5: 270 usec per loop - 100
# 100 loops, best of 5: 3.45 msec per loop - 500
# 100 loops, best of 5: 10.1 msec per loop - 1000
# 100 loops, best of 5: 356 msec per loop   - 9999

# cProfile.run('no_sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.011    0.011    0.011    0.011 task2.py:55(no_sieve)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Выводы:
# Алгоритм без использования «Решета Эратосфена» работает быстрее на относительно малых числах. Но с увеличением
# порядкового номера искомого числа среднее время поиска растет нелинейно.
# В то время как в алгоритме с использованием «Решета Эратосфена»
# среднее время выполнения алгоритма растет пропорционально порядковому номеру простого числа.



def test_value(func):
    lst = [-1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')
    assert func(MAX_LIMIT_NUMBER) == -1
    print(f'Test {MAX_LIMIT_NUMBER} OK')
    assert func(9999) == 104723
    print('Test 9999 OK')


# test_value(no_sieve)
# test_value(sieve)
#
# print(sieve(9999) == no_sieve(9999))
# print(no_sieve(9999))
# print(sieve(9999))
