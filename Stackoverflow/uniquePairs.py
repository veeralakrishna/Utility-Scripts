# Unique Combination Pairs for list of elements
def uniqueCombinations(numeric_col):
    l = list(itertools.combinations(numeric_col, 2))
    s = set(l)
    # print('actual', len(l), l)
    return list(s)
