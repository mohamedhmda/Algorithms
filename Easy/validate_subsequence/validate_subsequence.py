def isValidSubsequence(array, sequence):
    index = -1
    for s in sequence:
        if s in array:
            if index < array.index(s):
                index = array.index(s)
            else:
                return False
        else:
            return False
    return True

def isValidSubsequence2(array, sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

'''
print(sequence)
if isValidSubsequence(array,sequence):
    print("is a valid subsequence of")
else:
    print("is not a valid subsequence of")
print(array)
'''