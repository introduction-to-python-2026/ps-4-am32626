def split_before_each_uppercase(formula):
    prefix = ""
    uppercase = []
    for char in e:
        if char.isupper():
            if prefix != "":
                uppercase.append(prefix)
            prefix = char
        else:
            prefix += char
    if prefix != "":
        uppercase.append(prefix)
    return uppercase


def split_at_first_digit(formula):
    prefix = ""
    for char in s:
        if char.isdigit():
            return prefix, char
        prefix += char
    return prefix, "1"
    
