# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count_in_value(value: int, element: int) -> int:
    i = 0
    if value % 10 == element:
        i = 1

    if value // 10 == 0:
        return i
    else:
        return i + count_in_value(value // 10, element)


element = int(input('Введите цифру'))
count_list = int(input('Введите количество целых чисел в последовательности'))
result_count = 0
for i in range(count_list):
    value = int(input('Введите целое число'))
    result_count += count_in_value(value, element)
print(f'В последовательности чисел цифра {element} встречалась {result_count} раз')
