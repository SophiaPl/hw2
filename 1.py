filename = input('Input genome filename in FASTA format: ')

with open(filename, 'r') as file:
    for row in file:
        if '>' in row:
            print('\n', row.strip())
        else:
            print(row.strip(), end='')