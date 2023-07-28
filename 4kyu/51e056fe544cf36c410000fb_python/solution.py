import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"(?:'{1})?[a-z][a-z']*",text.lower(), flags=re.I)
    return [word for word, occurence in Counter(words).most_common(3) if occurence >= 1]