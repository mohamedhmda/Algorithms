import unittest

target = __import__("find_three_largest_numbers")

class TestFTLN(unittest.TestCase):
    def test_case_1(self):
        array = [-1, 3, 5, 8, 2, -9]
        largest_array = [8, 5, 3]
        result = target.find_three_largest_numbers(array)
        self.assertEqual(result, largest_array)
    
    def test_case_2(self):
        array = [1, 3, 5, 8, 2, 9]
        largest_array = [9, 8, 5]
        result = target.find_three_largest_numbers(array)
        self.assertEqual(result, largest_array)

if __name__ == "__main__":
    unittest.main()