# Also known as dichotomy search
def binary_search(array, m, target):
    le = len(array)
    mid = le//2
    if target < array[0] or target > array[le-1]:
        return -1
    if target == array[mid]:
        return m + mid
    elif target < array[mid]:
        return binary_search(array[0:mid],m , target)
    else: 
        return binary_search(array[mid:le],m+mid , target)


