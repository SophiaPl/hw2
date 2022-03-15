from collections import Counter

filename = input('Input genome filename in FASTA format: ')

with open(filename, 'r') as file:
    print(f"{'Name':<100} {'Length':<20} {'Symbol frequency:':<100}")
    sequences = {}
    for row in file:
        if '>' in row:
            name = row.strip()
            sequences[name] = ''
        else:
            sequences[name] += row.strip()
    for name, seq in sequences.items():
        print(f'{name:<100} {len(seq):<20} {str(dict(Counter(seq))):<100}')
