def expanded_form(num):
    num = str(num)
    return " + ".join(f"{n:<0{abs(i)}}" for i, n in enumerate(num, -len(num)) if n != '0')