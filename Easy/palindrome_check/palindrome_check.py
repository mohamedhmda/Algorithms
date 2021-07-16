# python easy way
def isPalindrome(string):
    return string == string[::-1]

# recursive approach
def palindrome_check(string, i, j):
    if j <= i:
        return True
    else:
        if string[i] == string[j]:
            return palindrome_check(string, i+1, j-1)
        else:
            return False

def isPalindrome2(string):
    return palindrome_check(string, 0, len(string)-1)
