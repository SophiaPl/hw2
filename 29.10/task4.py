number = int(input('Введите число: '))
dividers = []
for i in range(1, (number + 1)):
    if number % i == 0:
        dividers.append(i)
print(dividers)
