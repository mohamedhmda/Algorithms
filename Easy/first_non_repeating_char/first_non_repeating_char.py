def char_encoding(string):
    lenght = len(string)
    chars = []
    i = 0
    while i < lenght:
        char = string[i]
        count = 0
        while i < lenght and string[i] == char:
            i += 1
            count += 1
        exist = False
        for prev_char in chars:
            if prev_char[0] == char:
                prev_char[1] += count
                exist = True
                pass
        "" if exist else chars.append([char,count])
    return chars
    
def first_non_repeating_char(string):    
    chars = char_encoding(string)
    first_non_repeating_char = chars[0]
    for char in chars:
        if char[1] < first_non_repeating_char[1]:
            first_non_repeating_char = char
    return first_non_repeating_char[0]

