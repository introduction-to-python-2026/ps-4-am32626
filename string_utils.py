# string_utils.py

def split_before_each_uppercases(s: str) -> list:
    if not s:
        return []

    parts = []
    current = ""
    for ch in s:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch
    if current:
        parts.append(current)
    return parts

def split_at_first_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            j = i + 1
            while j < len(formula) and formula[j].isdigit():
                j += 1
            return formula[:i], int(formula[i:j])
    return formula, 1
