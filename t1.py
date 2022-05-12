filename = input('Input file name in FASTA format: ')

with open(filename, 'r') as file:
    for row in file:
        if '>' in row:
            print('\n', row.strip())  # вывод названия последовательности
        else:
            print(row.strip(), end='')  # вывод последовательности

