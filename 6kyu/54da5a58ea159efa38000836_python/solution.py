from collections import Counter

def find_it(seq):
    return next(k for k, v in Counter(seq).items() if v % 2)