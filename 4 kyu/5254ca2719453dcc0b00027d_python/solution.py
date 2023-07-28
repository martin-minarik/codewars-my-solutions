import itertools as it

def permutations(string):
    return list(dict.fromkeys("".join(p) for p in it.permutations(string, len(string))).keys())