import numpy as np
from math import log

print('Обозначения математических операций:\n+ - сложение\n- - вычитание\n* - умножение \
    \n/ - деление\n** - возведение в степень\nroot - извлечение корня\nlg - логарифмирование\n= - вывод результата\n')

# ввод списков и операций
bills = []
operation = []
oper = ''

while oper != '=':
    bills.append(list(map(float, input(f'Введите список из чисел через пробел: ').split())))
    oper = input('Введите математическую операцию: ')
    if oper != '+' and oper != '-' and oper != '*' and oper != '/' and oper != '**' and oper != 'root' and oper != 'lg' and oper != '=':
        print('\nТакой операции нет')
        exit()
    elif oper != '=':
        operation.append(oper)

if len(bills) < 2:
    print('\nВведён только один список\nРезультат вычисления: ', *bills[0])
    exit()

# выравнивание длин списков
max_len = 0
for i in range(len(bills)):
    if len(bills[i]) > max_len:
        max_len = len(bills[i])

for i in range(len(bills)):
    if len(bills[i]) < max_len:
        while len(bills[i]) < max_len:
            bills[i].insert(len(bills[i]), 0)

# np массивы, чтобы было легче считать
for i in range(len(bills)):
    bills[i] = np.array(bills[i])


# функция для подсчёта операций
def action(bill1, operation, bill2):
    if operation == '+':
        answer = bill1 + bill2
    elif operation == '-':
        answer = bill1 - bill2
    elif operation == '*':
        answer = bill1 * bill2
    elif operation == '/':
        answer = bill1 / bill2
    elif operation == '**':
        answer = bill1 ** bill2
    elif operation == 'root':
        units = [1] * max_len
        answer = bill1 ** (units / bill2)
    elif operation == 'lg':
        answer = []
        for i in range(max_len):
            answer.append(log(bill1[i], bill2[i]))
    return answer


# калькулятор списков
if len(bills) == 2:
    bill1, bill2 = bills[0], bills[1]
    op = operation[0]
    result = action(bill1, op, bill2)

elif len(bills) > 2:
    bill1, bill2 = bills[0], bills[1]
    op = str(operation[0])
    result = action(bill1, op, bill2)

    z = 1
    for i in range(2, len(bills)):
        bill1 = result
        bill2 = bills[i]
        op = operation[z]
        z += 1
        result = action(bill1, op, bill2)

print('\nРезультат вычисления: ', *np.round(result, 5))
