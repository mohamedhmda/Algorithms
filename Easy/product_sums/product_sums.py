def product_sums(array, depth):
    sum = 0
    for attribute in array:
        if isinstance(attribute, list):
            sum += ( depth + 1 ) * product_sums(attribute, depth +1)
        else:
            sum += attribute

    return sum
