def run_lenght_encoding(string):
    lenght = len(string)
    new_string = ""
    i = 0
    while i < lenght:
        char = string[i]
        count = 0
        while i < lenght and string[i] == char:
            i += 1
            count += 1
        new_string = ''.join([new_string,char,str(count)])


    return new_string    
    