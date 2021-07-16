def insertion_sort(array):
    l = len(array)
    for index in range(1,l):
        i = index
        j = i - 1
        while array[i] < array[j] and j >= 0:
            array[i], array[j] = array[j], array[i]
            j -= 1
            i -= 1

    return array