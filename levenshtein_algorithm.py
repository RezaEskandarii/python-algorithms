def levenshtein(str_a, str_b):
    if not str_a:
        return len(str_b)

    if not str_b:
        return len(str_a)

    return min(
        levenshtein(str_a[1:], str_b[1:]) + (str_a[0] != str_b[0]),
        levenshtein(str_a[1:], str_b) + 1
    )


print(levenshtein("Reza","Meza"))
