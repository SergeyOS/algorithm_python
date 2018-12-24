# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, то надо вывести число 6843.

def reverse_int(in_value: int, out_value: int) -> int:
    if in_value == 0:
        return out_value
    else:
        return reverse_int(in_value // 10, out_value * 10 + in_value % 10)


n = int(input('Введите положительное целое число:'))
result = reverse_int(n, 0)
print(f'Результат:{result}')
