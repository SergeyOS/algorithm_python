# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

start = 32
end = 127
i = 0
while start + i <= end:
    kod = start + i
    symbol = chr(kod)
    print(f'{kod}-"{symbol}"', end='\t')
    i += 1
    if i % 10 == 0:
        print('\n')
