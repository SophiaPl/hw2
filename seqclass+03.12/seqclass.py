class Sequence:

    def __init__(self, seq):
        if isinstance(seq, list):
            if len(seq) >= 2:  # последовательность введена с именем > и с \n
                self.name = seq[0]
                self.seq = seq[1].upper()
            else:
                self.name = None  # без имени
                self.seq = seq[0].upper()

        if isinstance(seq, str):  # последовательность введена в виде строки
            self.name = None
            self.seq = seq.upper()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration()
        element = self.seq[self.index]
        self.index += 1
        return element

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, item):
        return self.seq[item]

    def return_name(self):
        return self.name

    def return_seq(self):
        return self.seq

    def molstat(self):
        mol = self.alphabet
        stat = []
        for i in mol:
            stat.append((i, self.seq.count(i)))
        stat = dict(stat)
        return stat

    # метод, заменяющий A на *
    def replace(self):
        newseq = list(map(lambda x: '*' if x == 'A' else x, self.seq))
        return ''.join(newseq)

    # метод, заменяющий АA на A*
    def replace2(self):
        newseq = list(map(lambda x, y: '*' if x == 'A' and y == 'A' else x, self.seq[1:], self.seq))
        return ''.join(newseq)


class DNA(Sequence):

    @property
    def alphabet(self):
        return ['A', 'T', 'C', 'G']

    def molmass(self):
        mm = {'A': 313.21, 'T': 304.2, 'C': 289.18, 'G': 329.21}
        mass = -61.96
        for i in self.seq:
            mass += mm[i]
        return round(mass, 2)

    def complementary(self):
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ''
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq

    def transcription(self):
        d_rna = self.seq.replace('T', 'U')
        return d_rna


class RNA(Sequence):

    @property
    def alphabet(self):
        return ['A', 'U', 'C', 'G']

    def molmass(self):
        mm = {'A': 313.21, 'C': 289.18, 'G': 329.21, 'U': 306.2}
        mass = 159
        for i in self.seq:
            mass += mm[i]
        return round(mass, 2)

    def complementary(self):
        comp = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ''
        for i in self.seq:
            comp_seq += comp[i]
        return comp_seq

    @property
    def translation(self):
        codons = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
                  'CUG': 'L', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V',
                  'GUA': 'V', 'GUG': 'V', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P',
                  'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                  'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'stop',
                  'UAG': 'stop', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
                  'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C',
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
                    if protein:  # стоп-кодон
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


class Protein(Sequence):

    @property
    def alphabet(self):
        return ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

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

    # ввод
    my_seq = []
    x = ' '
    while x:
        x = input()
        my_seq.append(x)
    my_seq.remove('')

    # тип последовательности и преобразование к соотвествующему классу
    if 'A' in my_seq[-1] or 'T' in my_seq[-1] or 'C' in my_seq[-1] or 'G' in my_seq[-1]:
        check = 0
        for i in 'BDEFHIJKLMNOPQRSUVWXYZ':
            if i in my_seq[-1]:
                check += 1
                break
        if check == 0:
            mysamp = DNA(my_seq)

    if 'M' in my_seq[-1] or 'D' in my_seq[-1] or 'I' in my_seq[-1] or 'H' in my_seq[-1] or 'L' in my_seq[-1]:
        check = 0
        for i in 'BJOUXZ':
            if i in my_seq[-1]:
                check += 1
                break
        if check == 0:
            mysamp = Protein(my_seq)

    else:
        check = 0
        for i in 'BDEFHIJKLMNOPQRSTVWXYZ':
            if i in my_seq[-1]:
                check += 1
                break
        if check == 0:
            mysamp = RNA(my_seq)

    # методы
    print(type(mysamp))
    print(f'Название: {mysamp.return_name()}')
    print(f'Последовательность: {mysamp.return_seq()}')
    mysamp.__iter__()
    print(f'Длина: {mysamp.__len__()}')
    print(f'Next: {mysamp.__next__()}')
    print(f'Next +1: {mysamp.__next__()}')
    print(f'Next +1: {mysamp.__next__()}')
    print(f'Элемент с индексом 1: {mysamp.__getitem__(1)}')
    print(f'Алфавит: {mysamp.alphabet}')
    print(f'Статистика: {mysamp.molstat()}')
    print(f'Молекулярная масса: {mysamp.molmass()}')
    print(f'Замена A на *: {mysamp.replace()}')
    print(f'Замена AA на A*: {mysamp.replace2()}')

    if isinstance(mysamp, DNA):
        print(f'Комплементарная последовательность: {mysamp.complementary()}')
        print(f'Транскрипция: {mysamp.transcription()}')

    if isinstance(mysamp, RNA):
        print(f'Комплементарная последовательность: {mysamp.complementary()}')
        print(f'Трансляция: {mysamp.translation}')
