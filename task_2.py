# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
from operator import attrgetter


class HaffmanAlgorythm:
    code_dict: dict
    str_code = ''

    def encode(self, value: str):
        char_counter = Counter(value)
        root = Tree.fill_tree(char_counter)
        print(f'Tree value:{root}')
        self.str_code = ''
        self.code_dict = dict()
        Tree.fill_dictionary(root, self.code_dict, '')
        print(f'Dictionary:{sorted(self.code_dict.items(), key=lambda pair: len(pair[1]))}')
        for char in value:
            self.str_code += f'{self.code_dict[char]}'
        self.code_dict = dict(zip(self.code_dict.values(), self.code_dict.keys()))  # создаем тезареус после кодировки
        return self.str_code

    def decode(self):
        if self.str_code is None:
            return self.str_code
        result = ''
        spam_code = ''
        for i in self.str_code:
            spam_code += i
            if self.code_dict.get(spam_code) is not None:
                result += self.code_dict[spam_code]
                spam_code = ''
        return result


class Node:

    def __init__(self, weight=0, value=''):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None

    def __repr__(self):
        res = ''
        if self.left is not None:
            res += f'{self.left} '
        if self.right is not None:
            res += f'{self.right} '
        if self.left is None and self.right is None:
            res += f'\'{self.value}\':{self.weight}'
        return res


class Tree:
    # библиотека функций

    @staticmethod
    def create_leaf(element) -> Node:
        if type(element) == Node:
            return element
        else:
            return Node(weight=element[1], value=element[0])

    @staticmethod
    def create_node(first, second) -> Node:
        eggs = Node()
        eggs.left = Tree.create_leaf(first)
        eggs.right = Tree.create_leaf(second)
        eggs.weight = eggs.left.weight + eggs.right.weight
        return eggs

    @staticmethod
    def fill_dictionary(xnode: Node, result_dict: dict, path=''):
        if xnode.left is None and xnode.right is None:
            if len(path) == 0:
                result_dict[xnode.value] = '0'  # отлов строк из 1 символа
            else:
                result_dict[xnode.value] = path
        if xnode.left is not None:
            Tree.fill_dictionary(xnode.left, result_dict, path + '0')
        if xnode.right is not None:
            Tree.fill_dictionary(xnode.right, result_dict, path + '1')

    @staticmethod
    def fill_tree(spam_counter: Counter) -> Node:
        if len(spam_counter.items()) == 0:
            return Node()
        spam_list = list()
        for item in spam_counter.items():
            spam_list.append(Tree.create_leaf(item))
        spam_list.sort(key=attrgetter('weight'), reverse=True)
        while len(spam_list) > 1:
            element1 = spam_list.pop()
            element2 = spam_list.pop()
            eggs = Tree.create_node(element1, element2)
            spam_list.append(eggs)
            spam_list.sort(key=attrgetter('weight'), reverse=True)
        return spam_list[0]


STR_ENTER = 'practice makes perfect'
print(f'Исходная строка:\n{STR_ENTER}')
spam = HaffmanAlgorythm()
spam.encode(STR_ENTER)
print(f'Закодированная строка:\n{spam.str_code}')
str_result = spam.decode()
print(f'Раскодированная строка:\n{str_result}\nСтрока не изменилась:{STR_ENTER == str_result}')
