def sorted_square_array_with_sort(array):
    for n in range(len(array)):
        array[n] = array[n] * array[n]
    array.sort()
    return array

def sorted_square_array(array):
    new_array = []
    for n in range(len(array)):
        array[n] = array[n] * array[n]
        m = n
        while m > 0 and array[m] < array[m-1]:
            array[m], array[m-1] = array[m-1], array[m]
            m -= 1
    return array

    return array