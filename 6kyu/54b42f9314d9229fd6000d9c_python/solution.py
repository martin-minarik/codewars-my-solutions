from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return "".join('(' if counter[chr] == 1 else ')' for chr in word)