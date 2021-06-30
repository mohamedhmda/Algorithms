import unittest

target = __import__("non_constructible_change")

class TestNonConstructibleChange(unittest.TestCase):
    def test_case_1(self):
        array = [1, 3, 6, 10, 11, 15]
        result = target.non_constructible_change(array, 0, 0)
        self.assertEqual(result, 2)

    def test_case_2(self):
        array = [1, 1, 1, 1]
        result = target.non_constructible_change(array, 0, 0)
        self.assertEqual(result, 5)
    
    def test_case_3(self):
        array = [1, 1, 3, 4]
        result = target.non_constructible_change(array, 0, 0)
        self.assertEqual(result, 10)

    def test_case_4(self):
        array = [1, 2, 5, 10, 20, 40]
        result = target.non_constructible_change(array, 0, 0)
        self.assertEqual(result, 4)

    def test_case_5(self):
        array = [1, 2, 3, 4, 5, 6]
        result = target.non_constructible_change(array, 0, 0)
        self.assertEqual(result, 22)

if __name__ == '__main__':
    unittest.main()