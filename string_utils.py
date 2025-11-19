
def split_before_each_uppercase(formula):
    if not formula:
        return []
    result = []
    current_word = formula[0]
    for char in formula[1:]:
        if char.isupper():
            result.append(current_word)
            current_word = char
        else:
            current_word += char
    result.append(current_word)
    return result


def split_at_first_digit(formula):
    digit_location = 0
    for i, char in enumerate(formula):
      if char.isdigit():
         digit_location = i
         break
      if digit_location == 0:
         return formula, 1
      else:
        prefix = formula[:digit location]
        number = 
    int(formula[digit_locatio:])
        return prefix, number
    
