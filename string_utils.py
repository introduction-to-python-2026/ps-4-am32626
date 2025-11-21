def split_before_each_uppercase(formula):
    start = 0
    list_of_items = []
    for char in range(1, len(formula)):
        if formula[char].isupper():
            list_of_items.append(formula[start:char])
            start = char
    list_of_items.append(formula[start:])
    return list_of_items



def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1
    
