from collections import Counter
def first_non_repeating_letter(string):
    cc= Counter(string)
    return next((k for k, v in cc.items() if v == 1 and (not k.isalpha() or k.swapcase() not in cc)), '')