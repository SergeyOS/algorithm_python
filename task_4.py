# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

target_value = random.randint(0, 100)
max_count_enter = 10
num_enter = 0

while num_enter < max_count_enter:
    enter_value = int(input('Введите целое число'))
    num_enter += 1
    if target_value == enter_value:
        print(f'Вы угадали число {target_value} с {num_enter} попытки')
        break
    elif target_value < enter_value:
        print(f'Раунд  {num_enter}. Загаданное число меньше {enter_value}')
    else:
        print(f'Раунд  {num_enter}. Загаданное число больше {enter_value}')
else:
    print(f'Вы не угадали число {target_value} с {num_enter} попытки')
