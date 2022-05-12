from collections import Counter

filename = input('Input file name in FASTA format: ')

with open(filename, 'r') as file:
    n = 0
    sequences = {}

    for row in file:
        if '>' in row:
            if len(row) > int(n):
                n = str(len(row) + 5)  # n - длина самого длинного названия последовательности
            name = row.strip()
            sequences[name] = ''
        else:
            sequences[name] += row.strip()

    print(f"{'Name':<{n}} {'Length':<10} {'Symbol frequency:':<100}")
    for name, seq in sequences.items():
        print(f'{name:<{n}} {len(seq):<10} {str(dict(Counter(seq))):<100}')
