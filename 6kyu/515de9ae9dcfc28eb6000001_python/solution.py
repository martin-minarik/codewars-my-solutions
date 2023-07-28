import re
def solution(s):
    return [m if len(m) == 2 else m+'_' for m in map(lambda m: m.group(), re.finditer(r".{1,2}", s))] 