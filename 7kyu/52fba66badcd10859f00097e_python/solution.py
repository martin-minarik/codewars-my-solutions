import re

def disemvowel(string):
    return re.sub(r"[aeiou]", r"", string, flags=re.IGNORECASE)