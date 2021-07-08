import unittest

target = __import__('nth_fibonacci')

class TestFibonacci(unittest.TestCase):
    def test_case_1(self):
        result = target.nth_fibonacci(0)
        self.assertEqual(result, 0)

    def test_case_2(self):
        result = target.nth_fibonacci(1)
        self.assertEqual(result, 1)

    def test_case_3(self):
        result = target.nth_fibonacci(2)
        self.assertEqual(result, 1)
    
    def test_case_4(self):
        result = target.nth_fibonacci(5)
        self.assertEqual(result, 5)
    
    def test_case_5(self):
        result = target.nth_fibonacci(9)
        self.assertEqual(result, 34)

if __name__ == '__main__':
    unittest.main()