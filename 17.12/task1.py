def seqstat(func):
    def seqcount(*args):
        alph, seq = func(*args)
        stat = []
        for i in alph:
            stat.append((i, seq.count(i)))
        return dict(stat)

    return seqcount


@seqstat
def seqalph(seq):
    return list(set(seq)), seq


# проверка
if __name__ == '__main__':
    myseq = input('Введите последовательность: ')
    print(seqalph(myseq))
