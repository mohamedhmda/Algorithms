def bubble_sort(array):
    l = len(array)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(l-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False

    return array
