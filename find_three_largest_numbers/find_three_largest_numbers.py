def find_three_largest_numbers(array):
    largest_array = []
    for i in range(3):
        largest = array[0]
        for value in array:
            if value > largest:
                largest = value
        largest_array.append(largest)
        array.remove(largest)
    
    return largest_array
