# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input('Введите трехзначное целое число:'))
c1 = a % 10
c10 = (a % 100) // 10
c100 = a // 100
sum_values = c1 + c10 + c100
mult_values = c1 * c10 * c100
print(f'Сумма цифр = {sum_values}; произведение цифр ={mult_values}')
