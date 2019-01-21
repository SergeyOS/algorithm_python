# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict, deque

KEYS = '0123456789ABCDEF'


def init_dict(hex_is_key=True):
    # Иницирует словарь(hex_is_key=True) и тезаурус(hex_is_key=False)
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    if hex_is_key:
        result = defaultdict(lambda: None, zip(KEYS, values))
    else:
        result = defaultdict(lambda: None, zip(values, KEYS))
    return result


hex_to_int = init_dict()
int_to_hex = init_dict(False)


def hex_sum(a, b: deque):
    # Суммирует две очереди с шестнадцатеричными числами столбиком
    result = deque(a)
    next_step = 0
    while len(result) < len(b):
        result.appendleft('0')

    for j in range(len(b) - 1, -1, -1):
        spam = hex_to_int[result[j]] + hex_to_int[b[j]]
        spam = spam + next_step
        result[j] = int_to_hex[spam % 16]
        next_step = spam // 16
    while next_step > 0:
        result.appendleft(int_to_hex[next_step % 16])
        next_step = next_step // 16
    return delete_first_zero(result)


def hex_mult(a, b):
    # Перемножает две очереди с шестнадцатеричными числами столбиком
    result = deque(['0'])
    for i in range(len(a) - 1, -1, -1):
        result_i = deque(['0'] * (len(a) - 1 - i))  # хранит результат перемножения a[i] на b со сдвигом
        next_step = 0
        for j in range(len(b) - 1, -1, -1):
            spam = hex_to_int[a[i]] * hex_to_int[b[j]]
            spam = spam + next_step
            result_i.appendleft(int_to_hex[spam % 16])
            next_step = spam // 16
        while next_step > 0:
            result_i.appendleft(int_to_hex[next_step % 16])
            next_step = next_step // 16
        result = hex_sum(result, result_i)
    return delete_first_zero(result)


def delete_first_zero(res: deque) -> deque:
    # Удаляет лидирующие нули
    while res[0] == '0' and len(res) > 1:
        res.popleft()
    return res


def check_enter(s) -> bool:
    control_set = frozenset(KEYS)
    check_set = frozenset(s)
    return check_set.issubset(control_set)


str_input1 = input(f'Введите шестнадцатеричных число:').upper()
str_input2 = input(f'Введите шестнадцатеричных число:').upper()
if check_enter(str_input1) and check_enter(str_input2):
    a = deque(str_input1)
    b = deque(str_input2)
    print(f'Сумма чисел：{"".join(hex_sum(a, b))}')
    print(f'Произведение чисел：{"".join(hex_mult(a, b))}')
else:
    print('Ошибка ввода')
