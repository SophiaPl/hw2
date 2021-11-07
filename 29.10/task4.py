number = int(input('Введите число: '))
div = []
pr_f = []

for i in range(2, (number + 1)):
    if number % i != 0:
        continue
    else:
        div.append(i)

if len(div) == 1:
    print(div)
else:
    for j in div:
        for h in range(2, (j + 1)):
            if j % h == 0 and j == h:
                pr_f.append(j)
                break
        break
if (number / j) % j == 0:
    print(pr_f)
else:

