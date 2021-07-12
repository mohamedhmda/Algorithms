import unittest

target = __import__("palindrome_check")

class TestPalindromeCheck(unittest.TestCase):
    def test_case_1(self):
        string = "malayalam"
        result = target.isPalindrome(string)
        self.assertTrue(result)

    def test_case_2(self):
        string = "geeks"
        result = target.isPalindrome(string)
        self.assertFalse(result)

    def test_case_3(self):
        string = "malayalam"
        result = target.isPalindrome2(string)
        self.assertTrue(result)

    def test_case_4(self):
        string = "geeks"
        result = target.isPalindrome2(string)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()