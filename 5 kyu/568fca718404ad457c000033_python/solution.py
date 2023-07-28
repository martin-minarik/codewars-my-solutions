from itertools import pairwise

def find(seq):
    sorted_seq = sorted(seq)

    d1 = sorted_seq[1] - sorted_seq[0]
    d2 = sorted_seq[2] - sorted_seq[1]
    d3 = sorted_seq[3] - sorted_seq[2]

    d = d1 if d1 == d2 else d3

    return next((a + d for a, b in pairwise(sorted_seq) if (a + d) != b), seq[0])