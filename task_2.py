# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов:'))
if n > 0:
    sum_result = 1  # первый элемент
    koeff = 1
    for i in range(1, n):
        koeff = (-0.5) * koeff
        sum_result = sum_result + koeff
    print(f'Сумма ряда:{sum_result}')
else:
    print('Не удалось сформировать ряд')
