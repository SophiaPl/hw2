import random


# последовательность ДНК
def dnarandomseq():
    dnaseq = random.choices(['A', 'T', 'C', 'G'], k=random.randint(10, 1000))
    return ''.join(dnaseq)


# последовательность РНК
def rnarandomseq():
    rnaseq = random.choices(['A', 'U', 'C', 'G'], k=random.randint(10, 1000))
    return ''.join(rnaseq)


# аминокислотная последовательность
def protrandomseq():
    protseq = random.choices(
        ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'],
        k=random.randint(10, 1000))
    return ''.join(protseq)


# проверка
if __name__ == '__main__':
    print(dnarandomseq(), rnarandomseq(), protrandomseq(), sep='\n')
