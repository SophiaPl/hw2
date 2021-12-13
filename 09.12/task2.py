import random

dna = random.choice(['A', 'T', 'C', 'G'])
rna = random.choice(['A', 'U', 'C', 'G'])
prot = random.choice(
    ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])


# проверка
if __name__ == '__main__':
    print(dna, rna, prot, sep='\n')
