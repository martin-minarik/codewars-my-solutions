from heapq import nlargest

def two_highest(lst):
    return nlargest(2, set(lst))