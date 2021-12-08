import seqclass as sq
import inssort as ins


def seqsort(seq):
    stats = []
    for i in range(len(seq)):
        stats.append(seq[i].molstat())
    # print(stats)

    repl = []
    repl_in_seq = []
    for i in range(1, len(stats)):
        ra = abs(stats[0]['A'] - stats[i]['A'])  # [0] - референсная последовательность
        rt = abs(stats[0]['T'] - stats[i]['T'])
        rc = abs(stats[0]['C'] - stats[i]['C'])
        rg = abs(stats[0]['G'] - stats[i]['G'])
        repl.append(ra + rt + rc + rg)
        repl_in_seq.append((repl[-1], seq[i]))

    repl_in_seq = dict(repl_in_seq)
    sortrep = ins.inssort(repl)
    sortseq = [seq[0].return_seq()]
    for i in sortrep:
        sortseq.append(repl_in_seq[i].return_seq())

    return sortseq


# проверка
if __name__ == '__main__':
    lseq = []
    x = ' '
    while x:
        x = input()
        lseq.append(x)
    lseq.remove('')

    if 'A' in lseq[0] and 'T' in lseq[0] and 'C' in lseq[0] and 'G' in lseq[0]:
        for i in range(len(lseq)):
            lseq[i] = sq.DNA(lseq[i])

    elif 'A' in lseq[0] and 'U' in lseq[0] and 'C' in lseq[0] and 'G' in lseq[0]:
        for i in lseq:
            i = sq.RNA(i)

    else:
        for i in lseq:
            i = sq.Protein(i)

    s = seqsort(lseq)
    for i in s:
        print(i)
