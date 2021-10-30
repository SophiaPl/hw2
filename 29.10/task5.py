number = int(input('Введите число > 1: '))
first_two = []
while len(first_two) < 2:
    for i in range(number, 0, -1):
        for j in range(2, (number+1)):
            if i % j != 0:
                continue
            else:
                break
        if i == j:
            first_two.append(i)
            number = i - 1
            break
else:
    fib = sorted(first_two)
while len(fib) < 15:
    fib.append(fib[-2] + fib[-1])
print(fib)

