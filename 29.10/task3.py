number = int(input('Введите число > 2: '))
previous = number - 1
for i in range(previous, 1, -1):
    for j in range(2, number):
        if i % j != 0:
            continue
        else:
            break
    if i == j:
        break
print(i)
