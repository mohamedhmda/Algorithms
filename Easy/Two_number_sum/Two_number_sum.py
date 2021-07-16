def twosum_naive(array, sum):
    returnable = []
    for i in range(0,len(array)-1):
        for j in range(i+1, len(array)):
            if (array[i]+array[j]) == sum:
                returnable.append([array[i], array[j]])
    
    return returnable

def twosum_hashtable(array, sum):
    returnable = []
    hashtable = []
    for i in array:
        if i not in hashtable and (sum-i) != i and (sum-i) in array:
            returnable.append([i, sum-i])
            hashtable.append(sum-i)

    return returnable


array = [1, 2, -3, 4, -5, 6]
sum = 10
print(twosum_naive(array, sum))
print(twosum_hashtable(array, sum))

