class Sequence:

    def __init__(self, seq):
        self.seq = seq

    # возвращение последовательности
    def return_seq(self):
        return f'Последовательность: {self.seq}'

    # возвращение длины последовательности
    def __len__(self):
        return f'Длина последовательности: {len(self.seq)}'


# ДНК
class DNA(Sequence):

    # возвращение названия последовательности
    def return_name(self):
        return 'ДНК'

    # алфавит
    @property
    def DNA_alphabet(self):
        return 'A T C G'

    # статистика по использованию символов
    def DNA_molstat(self):
        GC = ((self.seq.count("C") + self.seq.count("G")) / len(self.seq)) * 100
        return f'Количественный состав: A - {self.seq.count("A")}, T - {self.seq.count("T")}, C - {self.seq.count("C")}, G - {self.seq.count("G")} \
    \nGC состав: {round(GC)} %'

    # молекулярная масса
    def DNA_molmass(self):
        m_A, m_T, m_C, m_G = 313.21, 304.2, 289.18, 329.21  # ММ нуклеотидов
        mass = self.seq.count("A") * m_A + self.seq.count("T") * m_T + self.seq.count("C") * m_C + self.seq.count("G") * m_G - 61.96
        return f'Молекулярная масса: {round(mass, 2)}'

    # комплементарная последовательность
    def DNA_complementary(self):
        comp_seq = ''
        for i in self.seq:
            if i == 'A':
                comp_seq += 'T'
            elif i == 'T':
                comp_seq += 'A'
            elif i == 'C':
                comp_seq += 'G'
            elif i == 'G':
                comp_seq += 'C'
        return f'Комплементарная последовательность: {comp_seq}'

    # транскрипция
    def transcription(self):
        d_RNA = ''
        for i in self.seq:
            if i == 'A':
                d_RNA += 'A'
            elif i == 'T':
                d_RNA += 'U'
            elif i == 'C':
                d_RNA += 'C'
            elif i == 'G':
                d_RNA += 'G'
        return f'Результат транскрипции: {d_RNA}'


# РНК
class RNA(Sequence):

    # возвращение названия последовательности
    def return_name(self):
        return 'РНК'

    # алфавит
    @property
    def RNA_alphabet(self):
        return 'A U C G'

    # статистика по использованию символов
    def RNA_molstat(self):
        GC = ((self.seq.count("C") + self.seq.count("G")) / len(self.seq)) * 100
        return f'Количественный состав: A - {self.seq.count("A")}, U - {self.seq.count("U")}, C - {self.seq.count("C")}, G - {self.seq.count("G")} \
    \nGC состав: {round(GC)} %'

    # молекулярная масса
    def RNA_molmass(self):
        m_A, m_U, m_C, m_G = 313.21, 306.2, 289.18, 329.21  # ММ нуклеотидов
        mass = self.seq.count("A") * m_A + self.seq.count("U") * m_U + self.seq.count("C") * m_C + self.seq.count("G") * m_G + 159.0
        return f'Молекулярная масса: {round(mass, 2)}'

    # комплементарная последовательность
    def RNA_complementary(self):
        comp_seq = ''
        for i in self.seq:
            if i == 'A':
                comp_seq += 'U'
            elif i == 'U':
                comp_seq += 'A'
            elif i == 'C':
                comp_seq += 'G'
            elif i == 'G':
                comp_seq += 'C'
        return f'Комплементарная последовательность: {comp_seq}'

    # трансляция РНК в белок
    def translation(self):
        codons = dict([('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'), ('CUU', 'L'), ('CUC', 'L'), ('CUA', 'L'),
                       ('CUG', 'L'), ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'), ('GUU', 'V'), ('GUC', 'V'),
                       ('GUA', 'V'), ('GUG', 'V'), ('UCU', 'S'), ('UCC', 'S'), ('UCA', 'S'), ('UCG', 'S'), ('CCU', 'P'),
                       ('CCC', 'P'), ('CCA', 'P'), ('CCG', 'P'), ('ACU', 'T'), ('ACC', 'T'), ('ACA', 'T'), ('ACG', 'T'),
                       ('GCU', 'A'), ('GCC', 'A'), ('GCA', 'A'), ('GCG', 'A'), ('UAU', 'Y'), ('UAC', 'Y'),
                       ('UAA', 'stop'), ('UAG', 'stop'), ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'G'), ('CAG', 'G'),
                       ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'), ('GAU', 'D'), ('GAC', 'D'),
                       ('GAA', 'E'), ('GAG', 'E'), ('UGU', 'C'), ('UGC', 'C'), ('UGA', 'stop'), ('UGG', 'W'),
                       ('CGU', 'R'), ('CGC', 'R'), ('CGA', 'R'), ('CGG', 'R'), ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'),
                       ('AGG', 'R'), ('GGU', 'G'), ('GGC', 'G'), ('GGA', 'G'), ('GGG', 'G')])
        protein = ''
        all_ORF = []
        ORF_in_one = []
        for i in 0, 1, 2:  # три ORF
            while i < (len(self.seq) - 2):
                cod = self.seq[i:i + 3]
                if codons.get(cod) != 'stop':
                    protein += codons.get(cod)
                    i += 3
                else:
                    if protein:  # если внутри ORF встретился стоп-кодон
                        ORF_in_one.append(protein)
                        protein = ''
                        i += 3
                    else:
                        i += 3
            else:
                ORF_in_one.append(protein)

                all_ORF.append(ORF_in_one)
                protein = ''
                ORF_in_one = []

        return f'Возможные рамки считывания: {all_ORF}'


# Белки
class Protein(Sequence):

    # возвращение названия последовательности
    def return_name(self):
        return 'Белок'

    # алфавит
    @property
    def P_alphabet(self):
        return 'A R N D C Q E G H I L K M F P S T W Y V'

    # статистика по использованию символов
    def P_molstat(self):
        A, R, N, D = self.seq.count("A"), self.seq.count("R"), self.seq.count("N"), self.seq.count("D")
        C, Q, E, G = self.seq.count("C"), self.seq.count("Q"), self.seq.count("E"), self.seq.count("G")
        H, I, L, K = self.seq.count("H"), self.seq.count("I"), self.seq.count("L"), self.seq.count("K")
        M, F, P, S = self.seq.count("M"), self.seq.count("F"), self.seq.count("P"), self.seq.count("S")
        T, W, Y, V = self.seq.count("T"), self.seq.count("W"), self.seq.count("Y"), self.seq.count("V")
        return f'Количественный состав: A - {A}, R - {R}, N - {N}, D - {D}, C - {C}, Q - {Q}, E - {E}, G - {G}, \
H - {H}, I - {I}, L - {L}, K - {K}, M - {M}, F - {F}, P - {P}, S - {S}, T - {T}, W - {W}, Y - {Y}, V - {V}'

    # молекулярная масса (?)
    def P_molmass(self):
        A, R, N, D = self.seq.count("A"), self.seq.count("R"), self.seq.count("N"), self.seq.count("D")
        C, Q, E, G = self.seq.count("C"), self.seq.count("Q"), self.seq.count("E"), self.seq.count("G")
        H, I, L, K = self.seq.count("H"), self.seq.count("I"), self.seq.count("L"), self.seq.count("K")
        M, F, P, S = self.seq.count("M"), self.seq.count("F"), self.seq.count("P"), self.seq.count("S")
        T, W, Y, V = self.seq.count("T"), self.seq.count("W"), self.seq.count("Y"), self.seq.count("V")

        # ММ аминокислот
        m_A, m_R, m_N, m_D = 89.09, 174.21, 132.12, 133.1
        m_C, m_Q, m_E, m_G = 121.15, 146.15, 147.13, 75.07
        m_H, m_I, m_L, m_K = 155.16, 131.17, 131.17, 146.19
        m_M, m_F, m_P, m_S = 149.21, 165.19, 115.13, 105.09
        m_T, m_W, m_Y, m_V = 119.12, 204.22, 181.2, 117.12

        mass = A * m_A + R * m_R + N * m_N + D * m_D + C * m_C + Q * m_Q + E * m_E + G * m_G + H * m_H + I * m_I \
               + L * m_L + K * m_K + M * m_M + F * m_F + P * m_P + S * m_S + T * m_T + W * m_W + Y * m_Y + V * m_V

        return f'Молекулярная масса: {round(mass, 2)}'


# проверка работоспособности этого всего
# ввод последовательности
my_seq = input('Введите последовательность: ').upper()

# ДНК
if 'A' in my_seq and 'T' in my_seq and 'C' in my_seq and 'G' in my_seq:
    if my_seq.isalpha():
        for i in 'BDEFHIJKLMNOPQRSUVWXYZ':
            if i in my_seq:
                print('В введённой последовательности ДНК присутствуют неподдерживаемые символы')
                exit()
    else:
        print('В введённой последовательности ДНК присутствуют неподдерживаемые символы')
        exit()

    DNA_samp = DNA(my_seq)
    print(DNA_samp.return_name())
    print(DNA_samp.return_seq())
    print(DNA_samp.DNA_alphabet)
    print(DNA_samp.__len__())
    print(DNA_samp.DNA_molstat())
    print(DNA_samp.DNA_molmass())
    print(DNA_samp.DNA_complementary())
    print(DNA_samp.transcription())

# РНК
elif 'A' in my_seq and 'U' in my_seq and 'C' in my_seq and 'G' in my_seq:
    if my_seq.isalpha():
        for i in 'BDEFHIJKLMNOPQRSTVWXYZ':
            if i in my_seq:
                print('В введённой последовательности РНК присутствуют неподдерживаемые символы')
                exit()
    else:
        print('В введённой последовательности РНК присутствуют неподдерживаемые символы')
        exit()

    RNA_samp = RNA(my_seq)
    print(RNA_samp.return_name())
    print(RNA_samp.return_seq())
    print(RNA_samp.RNA_alphabet)
    print(RNA_samp.__len__())
    print(RNA_samp.RNA_molstat())
    print(RNA_samp.RNA_molmass())
    print(RNA_samp.RNA_complementary())
    print(RNA_samp.translation())

# Белки
elif 'A' in my_seq or 'G' in my_seq or 'S' in my_seq or 'I' in my_seq or 'M' in my_seq:
    if my_seq.isalpha():
        for i in 'BJOUXZ':
            if i in my_seq:
                print('В введённой белковой последовательности присутствуют неподдерживаемые символы')
                exit()
    else:
        print('В введённой белковой последовательности присутствуют неподдерживаемые символы')
        exit()

    P_samp = Protein(my_seq)
    print(P_samp.return_name())
    print(P_samp.return_seq())
    print(P_samp.P_alphabet)
    print(P_samp.__len__())
    print(P_samp.P_molstat())
    print(P_samp.P_molmass())

else:
    print('Невозможно определить последовательность')