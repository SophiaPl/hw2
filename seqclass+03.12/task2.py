import seqclass
import inssort


def seqsort(seq):
    alph = seq[0].alphabet  # символы в последовательности

    stats = []
    for i in range(len(seq)):
        stats.append(seq[i].molstat())  # список со статистиками использования символов в каждой последовательности

    repl = []
    repl_and_seq = []
    for i in range(1, len(stats)):
        r = 0   # счётчик замен
        for j in alph:
            r += abs(stats[0][j] - stats[i][j])    # [0] - референсная последовательность
        repl.append(r)  # суммарное количество замен в последовательности
        repl_and_seq.append((repl[-1], seq[i]))  # количество замен и соотвествующая последовательность

    repl_in_seq = dict(repl_and_seq)
    sortrep = inssort.inssort(repl)  # сортировка по количеству замен
    sortseq = [seq[0].return_seq()]  # начало для отсортированного списка с последовательностями (референс первый)
    for i in sortrep:
        sortseq.append(
            repl_in_seq[i].return_seq())  # добавление в список последовательностей с вощрастающим числом замен

    return sortseq


# проверка
if __name__ == '__main__':

    # ввод
    lseq = []
    x = ' '
    while x:
        x = input()
        lseq.append(x)
    lseq.remove('')

    # тип последовательности и преобразование к соотвествующему классу
    if 'A' in lseq[0] or 'T' in lseq[0] or 'C' in lseq[0] or 'G' in lseq[0]:
        check = 0
        for i in 'BDEFHIJKLMNOPQRSUVWXYZ':
            if i in lseq[0]:
                check += 1
                break
        if check == 0:
            for i in range(len(lseq)):
                lseq[i] = seqclass.DNA(lseq[i])

    if 'M' in lseq[0] or 'D' in lseq[0] or 'I' in lseq[0] or 'H' in lseq[0] or 'L' in lseq[0]:
        check = 0
        for i in 'BJOUXZ':
            if i in lseq[0]:
                check += 1
                break
        if check == 0:
            for i in range(len(lseq)):
                lseq[i] = seqclass.Protein(lseq[i])

    else:
        check = 0
        for i in 'BDEFHIJKLMNOPQRSTVWXYZ':
            if i in lseq[0]:
                check += 1
                break
        if check == 0:
            for i in range(len(lseq)):
                lseq[i] = seqclass.RNA(lseq[i])


    # сортировка
    s = seqsort(lseq)
    for i in s:
        print(i)
