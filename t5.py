import os.path
import re
from Bio.Seq import Seq


def file_reader(filename: str):
    if not filename:
        raise TypeError("Missing required argument: 'filename'")
    elif not os.path.exists(filename):
        raise FileNotFoundError(f'File name {filename} is not defined')
    elif not isinstance(filename, str):
        raise TypeError('File name must be a string')
    elif '.fa' not in filename:
        raise TypeError('File must be in FASTA format')
    else:
        with open(filename, 'r') as file:
            result = {}
            name = ''
            for row in file:
                try:
                    if '>' in row:
                        name = row.strip('\n')
                        result[name] = ''
                    else:
                        result[name] += row.strip('\n')
                except KeyError:
                    print(f'Sequence name started with ">" is not defined')
    return result


def frames_creator(seq: str):
    if not seq:
        raise TypeError("Missing required argument: 'seq'")
    if not isinstance(seq, str):
        raise TypeError('Sequence must be a string')
    try:
        fr1, fr2, fr3 = seq, seq[1:], seq[2:]
        rev_code = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'B': 'V', 'D': 'H', 'H': 'D', 'K': 'M',
                    'M': 'K', 'N': 'N', 'R': 'Y', 'S': 'S', 'V': 'B', 'W': 'W', 'Y': 'R'}
        seq = '_' + seq
        rev_seq = ''.join([rev_code[i] for i in seq[-1:0:-1]])
        fr4, fr5, fr6 = rev_seq, rev_seq[1:], rev_seq[2:]
        return fr1, fr2, fr3, fr4, fr5, fr6
    except KeyError:
        print('Unexpected symbol in sequence')


def orf_translate(orf_list: list):
    for i in range(len(orf_list)):
        seq_orf = Seq(orf_list[i])
        orf_list[i] = str(seq_orf.translate())
    return orf_list


def orf_finder(seq: str):
    if not seq:
        raise TypeError("Missing required argument: 'seq'")
    if not isinstance(seq, str):
        raise TypeError('Sequence must be a string')
    pattern = r'(ATG.+?)(TAA|TAG|TGA)'
    orfs = []
    for fr in frames_creator(seq):
        frame = ''
        for n in range(0, len(fr) + 1, 3):
            if len(fr[n:n + 3]) == 3:
                frame += fr[n:n + 3] + '_'
        result = re.findall(pattern, frame)
        for i in result:
            if len((i[0]).replace('_', '')) >= 300:
                orfs.append((i[0]).replace('_', ''))
    orf_tr = orf_translate(orfs)
    return orf_tr


def orfdict(orf_tr: list):
    orf_dict = {}
    for i in range(len(orf_tr)):
        orf_dict['ORF'+str(i+1)] = orf_tr[i]
    return orf_dict


if __name__ == '__main__':
    filename = input('Input filename in FASTA format: ')
    for name, seq in file_reader(filename).items():
        print()
        print(name)
        print(seq)
        for key, val in (orfdict(orf_finder(seq))).items():
            print(key, '\t', val)
