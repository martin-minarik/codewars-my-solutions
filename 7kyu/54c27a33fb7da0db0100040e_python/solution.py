def is_square(n):
    return (n ** (1/2)).is_integer() if n >= 0 else False