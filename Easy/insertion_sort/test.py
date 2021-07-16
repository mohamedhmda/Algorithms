import unittest

target = __import__("insertion_sort")


class TestInsertionSort(unittest.TestCase):
    def test_case_1(self):
        array = [4, 3, 2, 10, 12, 1, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6, 10, 12]
        result = target.insertion_sort(array)
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        array = [12, 11, 13, 5, 6]
        expected_result = [5, 6, 11, 12, 13]
        result = target.insertion_sort(array)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()