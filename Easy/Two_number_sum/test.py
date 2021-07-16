import unittest

target = __import__("Two_number_sum")

class Test_Naive_Sum(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, 2, -4, 8, 11]
        sum = 7
        result = target.twosum_naive(array, sum)
        self.assertEqual(result, [[5, 2], [-4, 11]])

    def test_case_2(self):
        array = [3, 5, 2, -4, 8, 11]
        sum = 6
        result = target.twosum_naive(array, sum)
        self.assertEqual(result, [])

    def test_case_3(self):
        array = [1, 2, -3, 4, -5, 6]
        sum = 10
        result = target.twosum_naive(array, sum)
        self.assertEqual(result, [[4,6]])

class Test_Hash_Sum(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, 2, -4, 8, 11]
        sum = 7
        result = target.twosum_hashtable(array, sum)
        self.assertEqual(result, [[5, 2], [-4, 11]])

    def test_case_2(self):
        array = [3, 5, 2, -4, 8, 11]
        sum = 6
        result = target.twosum_hashtable(array, sum)
        self.assertEqual(result, [])

    def test_case_3(self):
        array = [1, 2, -3, 4, -5, 6]
        sum = 10
        result = target.twosum_hashtable(array, sum)
        self.assertEqual(result, [[4,6]])


if __name__ == '__main__':
    unittest.main()