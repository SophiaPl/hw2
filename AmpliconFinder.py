import re


def pattern_creator(forward, reverse):
    if not all((forward, reverse)):
        raise TypeError('Missing required argument')
    if not isinstance(forward, str) or not isinstance(reverse, str):
        raise TypeError('Primer must be a string')

    forward, reverse = forward.upper(), reverse.upper()
    forwdcode = {'A': 'A', 'T': 'T', 'C': 'C', 'G': 'G', 'B': '[CGT]', 'D': '[AGT]', 'H': '[ACT]', 'K': '[GT]',
                 'M': '[AC]', 'N': '[ACGT]', 'R': '[GA]', 'S': '[GC]', 'V': '[ACG]', 'W': '[AT]', 'Y': '[CT]'}
    revcode = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'B': '[GCA]', 'D': '[TCA]', 'H': '[TGA]', 'K': '[CA]',
               'M': '[TG]', 'N': '[ACGT]', 'R': '[CT]', 'S': '[CG]', 'V': '[TGC]', 'W': '[TA]', 'Y': '[GA]'}
    pattern = ''

    try:
        for i in forward:
            pattern += forwdcode[i]
        pattern += '.+'
        for j in reversed(reverse):
            pattern += revcode[j]
        return pattern
    except KeyError:
        print('Unexpected symbol in primer sequence')


def amplicon_finder(filename, pattern):
    if not all((filename, pattern)):
        raise TypeError('Missing required argument')
    if not isinstance(filename, str) or not isinstance(pattern, str):
        raise TypeError('Filename and pattern must be a string')
    if '.fa' not in filename:
        raise NameError('File must be in FASTA format')

    try:
        file = open(filename, 'r')
        genome = ''
        for row in file:
            if '>' not in row:
                genome += row.strip()
            else:
                genome += '\n' + row
        result = re.findall(pattern, genome)
        file.close()
        return result
    except FileNotFoundError:
        print('No such file')


if __name__ == '__main__':
    my_forward = input('Input forward primer: ')
    my_reverse = input('Input reverse primer: ')
    my_pattern = pattern_creator(my_forward, my_reverse)
    my_filename = input('Input genome filename in FASTA format: ')
    my_amplicon = amplicon_finder(my_filename, my_pattern)
    for i in my_amplicon:
        print(i)
