filename = input('Input genome filename in FASTA format: ')

with open(filename, 'r') as file:
    for raw in file:
        if '>' in raw:
            print('\n', raw.strip())
        else:
            print(raw.strip(), end='')