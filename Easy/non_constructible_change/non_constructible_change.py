def non_constructible_change(array, n, previousSum):
    if n == 0:
        array.sort()
    if n >= len(array) or array[n] - previousSum > 1:
        return previousSum + 1
    else:
        previousSum += array[n]
        n += 1
        return non_constructible_change(array, n, previousSum)

