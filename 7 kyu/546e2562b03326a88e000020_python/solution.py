def square_digits(num):
    return int("".join(map(str, [num ** 2 for num in map(int, str(num))])))