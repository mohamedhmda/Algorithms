def selections_sort(array):
    l = len(array)
    for i in range(l-1):
        for j in range(i,l):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array