number = int(input('Введите число > 2: '))
previous = number - 1
while previous < number:
    for i in range(previous, 1, -1):
        for j in range(2, number):
            if i % j != 0:
                continue
            else:
                break
        if i == j:
            break
        else:
            continue
    previous += number
    # как-то не по-умному, но я не знаю, как ещё остановить цикл
else:
    print(i)
