import unittest

target = __import__("product_sums")

class TestProductSums(unittest.TestCase):
    def test_case_1(self):
        array = [3, [4, 5]]
        initial_depth = 1
        result = target.product_sums(array, initial_depth)
        self.assertEqual(result, 21)

    def test_case_2(self):
        array = [6, [4, [5]]]
        initial_depth = 1
        result = target.product_sums(array, initial_depth)
        self.assertEqual(result, 44)

if __name__ == '__main__':
    unittest.main()