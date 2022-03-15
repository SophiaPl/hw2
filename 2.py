from collections import Counter

filename = input('Input genome filename in FASTA format: ')

with open(filename, 'r') as file:
    print(f"{'Name':<100} {'Length':<20} {'Symbol frequency:':<100}")
    sequences = {}
    for raw in file:
        if '>' in raw:
            name = raw.strip()
            sequences[name] = ''
        else:
            sequences[name] += raw.strip()
    for name, seq in sequences.items():
        print(f'{name:<100} {len(seq):<20} {str(dict(Counter(seq))):<100}')
