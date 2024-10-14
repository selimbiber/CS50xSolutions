from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    lines_a = set(a.splitlines())
    lines_b = set(b.splitlines())
    return list(lines_a.intersection(lines_b))

def sentences(a, b):
    """Return sentences in both a and b"""
    sentences_a = set(sent_tokenize(a))
    sentences_b = set(sent_tokenize(b))
    return list(sentences_a.intersection(sentences_b))

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    substrings_a = {a[i:i+n] for i in range(len(a) - n + 1)}
    substrings_b = {b[i:i+n] for i in range(len(b) - n + 1)}
    return list(substrings_a.intersection(substrings_b))
