def dig_pow(n, p):
    digits_iter = map(int, str(n))
    sum_ = sum(digit ** exp for exp, digit in enumerate(digits_iter, start = p))
    return sum_ // n if not sum_ % n else -1