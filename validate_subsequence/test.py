import unittest
from unittest import result

target = __import__("validate_subsequence")

class Test_Naive_Sum(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        result = target.isValidSubsequence(array,sequence)
        self.assertEqual(result, True)

    def test_case_2(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 6, -1, 8, 10]
        result = target.isValidSubsequence(array,sequence)
        self.assertEqual(result, True)

    def test_case_3(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [22, 25, 6]
        result = target.isValidSubsequence(array,sequence)
        self.assertEqual(result, True)

    def test_case_4(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, 10]
        result = target.isValidSubsequence(array,sequence)
        self.assertEqual(result, True)

    def test_case_5(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 10, 6]
        result = target.isValidSubsequence(array,sequence)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
