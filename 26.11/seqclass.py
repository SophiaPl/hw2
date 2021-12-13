class Sequence:

    def __init__(self, seq):
        self.samp = seq
        if isinstance(seq, str):
            self.seq = seq
        elif isinstance(seq, list):
            if len(seq) >= 2:
                self.name = seq[0]
                self.seq = seq[1]
            else:
                self.seq = seq[-1]

    # возвращение названия последовательности
    def return_name(self):
        if isinstance(self.samp, list):
            if len(self.samp) >= 2:
                return self.name
        else:
            return None

    # возвращение последовательности
    def return_seq(self):
        return self.seq

    # возвращение длины последовательности
    def __len__(self):
        return len(self.seq)

    # статистика по использованию символов
    def molstat(self):
        mol = self.alphabet
        stat = []
        for i in mol:
            stat.append((i, self.seq.count(i)))
        stat = dict(stat)
        return stat


# ДНК
class DNA(Sequence):

    # алфавит
    @property
    def alphabet(self):
        return ['A', 'T', 'C', 'G']

    # молекулярная масса
    def molmass(self):
        mm = {'A': 313.21, 'T': 304.2, 'C': 289.18, 'G': 329.21}
        mass = -61.96
        for i in self.seq:
            mass += mm[i]
        return round(mass, 2)

    # комплементарная последовательность
    def complementary(self):
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ''
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq

    # транскрипция
    def transcription(self):
        d_rna = self.seq.replace('T', 'U')
        return d_rna


# РНК
class RNA(Sequence):

    # алфавит
    @property
    def alphabet(self):
        return ['A', 'U', 'C', 'G']

    # молекулярная масса
    def molmass(self):
        mm = {'A': 313.21, 'C': 289.18, 'G': 329.21, 'U': 306.2}
        mass = 159
        for i in self.seq:
            mass += mm[i]
        return round(mass, 2)

    # комплементарная последовательность
    def complementary(self):
        comp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ''
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq

    # трансляция РНК в белок
    @property
    def translation(self):
        codons = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
                  'CUG': 'L', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V',
                  'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P',
                  'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                  'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'stop',
                  'UAG': 'stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'G', 'CAG': 'G', 'AAU': 'N', 'AAC': 'N',
                  'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'Q', 'GAG': 'Q', 'UGU': 'C',
                  'UGC': 'C', 'UGA': 'stop', 'UGG': 'W', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                  'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
        protein = ''
        all_orf = []
        orf_in_one = []
        for i in range(3):  # три ORF
            for j in range(i, len(self.seq) - 2, 3):
                cod = self.seq[j:j + 3]
                if codons[cod] != 'stop':
                    protein += codons[cod]
                else:
                    if protein:  # если внутри ORF встретился стоп-кодон
                        orf_in_one.append(protein)
                        protein = ''

            orf_in_one.append(protein)

            all_orf.append(orf_in_one)
            protein = ''
            orf_in_one = []

        for i in all_orf:
            if isinstance(i, list):
                for j in i:
                    j = Protein(j)
            else:
                i = Protein(i)

        return all_orf


# Белки
class Protein(Sequence):

    @property
    def alphabet(self):
        return ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

    # молекулярная масса
    def molmass(self):
        mm = {'A': 71.09, 'R': 156.21, 'N': 114.12, 'D': 115.1, 'C': 103.15,
              'Q': 128.15, 'E': 129.13, 'G': 57.07, 'H': 137.16, 'I': 113.17,
              'L': 113.17, 'K': 128.19, 'M': 131.21, 'F': 147.19, 'P': 97.13,
              'S': 87.09, 'T': 101.12, 'W': 186.22, 'Y': 163.2, 'V': 99.12}
        mass = 18
        for i in self.seq:
            mass += mm[i]
        return round(mass, 2)


# проверка
if __name__ == '__main__':

    my_seq = []
    x = ' '
    while x:
        x = input()
        my_seq.append(x)
    my_seq.remove('')

    if 'A' in my_seq[-1] and 'T' in my_seq[-1] and 'C' in my_seq[-1] and 'G' in my_seq[-1]:
        samp = DNA(my_seq)

    elif 'A' in my_seq[-1] and 'U' in my_seq[-1] and 'C' in my_seq[-1] and 'G' in my_seq[-1]:
        samp = RNA(my_seq)

    else:
        samp = Protein(my_seq)

    print(type(samp))
    print(f'Название: {samp.return_name()}')
    print(f'Последовательность: {samp.return_seq()}')
    print(f'Алфавит: {samp.alphabet}')
    print(f'Длина: {samp.__len__()}')
    print(f'Статистика: {samp.molstat()}')
    print(f'Молекулярная масса: {samp.molmass()}')

    if isinstance(samp, DNA):
        print(f'Комплементарная последовательность: {samp.complementary()}')
        print(f'Транскрипция: {samp.transcription()}')

    if isinstance(samp, RNA):
        print(f'Комплементарная последовательность: {samp.complementary()}')
        print(f'Трансляция: {samp.translation}')
