# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


def sum_elemets(value: int) -> int:
    if value == 0:
        return 0
    else:
        return value % 10 + sum_elemets(value // 10)


value = int(input('Введите натуральное число или 0 для выхода'))
max_sum = 0
max_value = 0
while value != 0:
    cur_sum = sum_elemets(value)
    if max_sum < cur_sum:
        max_sum = cur_sum
        max_value = value
    value = int(input('Введите натуральное число или 0 для выхода'))

if max_sum != 0:
    print(f'Число {max_value} c максимальной суммой цифр {max_sum}')