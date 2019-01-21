# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple, deque

TESTING = False
if TESTING:
    # использовать для тестирования на больших объемах
    import random

    MIN_VALUE = -100
    MAX_VALUE = 100

Company = namedtuple('Company', 'name, quarter1, quarter2, quarter3, quarter4 , year')
count_company = int(input('Введите количесиво предприятий:'))
if count_company >= 1:

    total = Company('total', 0, 0, 0, 0, 0)
    deq_company = deque()
    for i in range(count_company):  # формируем очередь предприятий и агрегирующие суммы
        name, q1, q2, q3, q4 = '', 0, 0, 0, 0
        if TESTING:
            # при тестировании на больших объемах
            name = i
            q1 = random.uniform(MIN_VALUE, MAX_VALUE)
            q2 = random.uniform(MIN_VALUE, MAX_VALUE)
            q3 = random.uniform(MIN_VALUE, MAX_VALUE)
            q4 = random.uniform(MIN_VALUE, MAX_VALUE)
            spam_company = Company(name, q1, q2, q3, q4, q1 + q2 + q3 + q4)
            print(f'{spam_company}')
        else:
            name = input('Введите наименование компании: ')
            q1 = float(input('Введите прибыль за 1 квартал: '))
            q2 = float(input('Введите прибыль за 2 квартал: '))
            q3 = float(input('Введите прибыль за 3 квартал: '))
            q4 = float(input('Введите прибыль за 4 квартал: '))
            spam_company = Company(name, q1, q2, q3, q4, q1 + q2 + q3 + q4)

        total = total._replace(quarter1=total.quarter1 + q1, quarter2=total.quarter2 + q2,
                               quarter3=total.quarter3 + q3, quarter4=total.quarter4 + q4,
                               year=total.year + q1 + q2 + q3 + q4)
        deq_company.append(spam_company)

    if TESTING:
        print(f'Список команий{deq_company}')

    avg_year_profit = total.year / count_company
    up_avg = deque()
    under_avg = deque()

    if TESTING:
        print(f'Средняя годовая прибыль {avg_year_profit}')

    for i in range(count_company):
        if avg_year_profit < deq_company[i].year:  # выше среднего
            up_avg.append(deq_company[i].name)
        elif avg_year_profit > deq_company[i].year:  # ниже среднего
            under_avg.append(deq_company[i].name)
        # else:  # компании со средней прибылью не нужны
    if len(up_avg) > 0 or len(under_avg):
        print(f'Компании с годовой прибылью выше среднего:  {up_avg}')
        print(f'Компании с годовой прибылью ниже среднего: {under_avg}')
    # else:
    #     print(f'У всех компаний средняя прибыль {deq_company}')
