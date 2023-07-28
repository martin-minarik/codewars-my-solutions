from math import log


def zeros(n):
    return n and sum(n // int(5 ** exp) for exp in range(1, int(log(n, 5)+1)))