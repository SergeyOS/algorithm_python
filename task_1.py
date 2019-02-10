# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

from collections import Counter


def is_only_need_char(value: str) -> bool:
    for i in value:
        if i < 'a' or i > 'z':
            return False
    return True


str_enter = input('Введите строку только из маленьких латинских букв:')
if is_only_need_char(str_enter):
    result = Counter()
    len_enter = len(str_enter)
    for len_sub in range(1, len_enter + 1):
        for index in range(len_enter - len_sub + 1):
            sub_str = str_enter[index:index + len_sub]
            hash_key = hash(sub_str.encode('utf-8'))
            if result[hash_key] == 0:
                print(f'{sub_str}:len = {len_sub}:index={index}')
            result[hash_key] += 1

    print(f'В строке {str_enter} различных подстрок:{len(result.items())}')
else:
    print(f'Строка нарушает условия задачи')
