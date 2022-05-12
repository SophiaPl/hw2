from math import ceil
from t5 import *


def isedge(orf1, orf2):
    minseq, maxseq = sorted((orf1, orf2), key=len)
    sub = ceil(len(minseq) * 0.8)
    for i in range(0, len(minseq)):
        if sub <= len(minseq):
            if minseq[i: sub] in maxseq:
                return True
            sub += 1
        else:
            return False


def makegraph(orf_list: list):
    orfs = [['ORF'+str(i+1), orf_list[i]] for i in range(len(orf_list))]
    graph = {}
    for i in orfs:
        graph[i[0]] = []
        compare = orfs.copy()
        compare.remove(i)
        for j in compare:
            if isedge(i[1], j[1]):
                graph[i[0]].append(j[0])
    return graph


def ccsearch(graph: dict):
    visited = {i: False for i in graph.keys()}
    cc = []

    def dfs(node):
        visited[node] = True
        if graph[node]:
            path.append(node)
            for neigh in graph[node]:
                if not visited[neigh]:
                    dfs(neigh)
            if path not in cc:
                cc.append(path)
        else:
            cc.append([node])

    for orf in graph.keys():
        path = []
        dfs(orf)

    return cc


if __name__ == '__main__':
    filename = input('Input filename in FASTA format: ')
    for name, seq in file_reader(filename).items():
        print()
        print(name)
        for i in sorted(ccsearch(makegraph(orf_finder(seq))), key=len, reverse=True):
            c = [j for j in i]
            print(*c, sep='---')
