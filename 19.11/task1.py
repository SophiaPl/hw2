import numpy as np
from math import log, e

print('Обозначения математических операций:\n+ - сложение\n- - вычитание\n* - умножение \
    \n/ - деление\n** - возведение в степень\nroot - извлечение корня\nlg - логарифмирование\n= - вывод результата\n')

# ввод списков
print('Введите список из чисел через пробел или нажмите Enter, чтобы прекратить ввод')

lists = []
input_list = [0]
while input_list:
    input_list = list(map(float, input('Введите список: ').split()))
    lists.append(input_list)
lists.remove([])

# ввод операции
op = input('\nВведите математическую операцию: ')


# выравнивание длин списков
def align(lists):
    max_len = 0
    for i in range(len(lists)):
        if len(lists[i]) > max_len:
            max_len = len(lists[i])

    for i in range(len(lists)):
        if len(lists[i]) < max_len:
            while len(lists[i]) < max_len:
                if op == '+' or op == '-' or op == '*' or op == '**':
                    lists[i].insert(len(lists[i]), 0)
                elif op == '/' or op == 'root':
                    lists[i].insert(len(lists[i]), 1)
                elif op == 'lg':
                    lists[i].insert(len(lists[i]), e)

    for i in range(len(lists)):
        lists[i] = np.array(lists[i])


# сложение
def adder(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = list1 + list2
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 + list2
    return answer


# вычитание
def deduction(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = list1 - list2
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 - list2
    return answer


# умножение
def multiplication(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = list1 * list2
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 * list2
    return answer


# деление
def division(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = list1 / list2
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 / list2
    return answer


# возведение в степень
def exponentation(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = list1 ** list2
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 ** list2
    return answer


# извлечение корня
def root(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    units = [1] * len(list1)
    answer = list1 ** (units / list2)
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        answer = list1 ** (units / list2)
    return answer


# логарифмирование
def logarithm(lists):
    align(lists)
    list1, list2 = lists[0], lists[1]
    answer = []
    for i in range(len(list1)):
        answer.append(log(list1[i], list2[i]))
    for i in range(2, len(lists)):
        list1 = answer
        list2 = lists[i]
        for i in range(len(list1)):
            answer.append(log(list1[i], list2[i]))
    return answer


# калькулятор
if op == '+':
    print(*adder(lists))
elif op == '-':
    print(*deduction(lists))
elif op == '*':
    print(*multiplication(lists))
elif op == '/':
    print(*division(lists))
elif op == '**':
    print(*exponentation(lists))
elif op == 'root':
    print(*root(lists))
elif op == 'lg':
    print(*logarithm(lists))
