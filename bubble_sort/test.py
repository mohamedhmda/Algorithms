import unittest

target = __import__("bubble_sort")

class TestBubbleSort(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2, 8]
        sorted = [1, 2, 4, 5, 8]
        result = target.bubble_sort(array)
        self.assertEqual(result, sorted)

    def test_case_2(self):
        array = [3, 5, 2, 4, 1]
        sorted = [1, 2, 3, 4, 5]
        result = target.bubble_sort(array)
        self.assertEqual(result, sorted)

if __name__ == "__main__":
    unittest.main()