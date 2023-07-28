def vert_mirror(strng):
    return '\n'.join([line[::-1] for line in strng.splitlines()])


def hor_mirror(strng):
    return '\n'.join(strng.splitlines()[::-1])
    
    
def oper(fct, s):
    return fct(s)