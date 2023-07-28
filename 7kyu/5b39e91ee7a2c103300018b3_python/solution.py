import itertools as it

def remove_consecutive_duplicates(s):
    return " ".join(key for key, _ in it.groupby(s.split()))