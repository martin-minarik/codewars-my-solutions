from functools import reduce
import operator
from math import factorial
from collections import Counter

def list_position(word):
    """Return the anagram list position of the word"""
    
    chars = sorted(set(word))

    if len(chars) <= 1:
        return 1

    frequencies = Counter(word)
    skipped = 0  # skipped permutations
    numerator = factorial(len(word) - 1)

    for c in chars:
        if c == word[0]:
            break

        frequencies[c] -= 1
        denominator = reduce(operator.mul, map(factorial, frequencies.values()))
        skipped += numerator // denominator
        frequencies[c] += 1

    return skipped + list_position(word[1:])