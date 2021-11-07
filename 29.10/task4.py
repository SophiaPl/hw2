number = int(input('Введите число > 1: '))
pr_n = []
pr_f = []
for i in range(number, 1, -1):
    for j in range(2, (number + 1)):
        if i % j != 0:
            continue
        else:
            break
    if i == j:
        pr_n.append(i)
for j in pr_n:
    if number % j == 0:
        pr_f.append(j)
print(sorted(pr_f))

