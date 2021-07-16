import unittest

target = __import__("binary_search")

class TestBinarySearch(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 1)
        self.assertEqual(result, 0)
    
    def test_case_2(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 2)
        self.assertEqual(result, 1)
    
    def test_case_3(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 3)
        self.assertEqual(result, 2)

    def test_case_4(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 4)
        self.assertEqual(result, 3)

    def test_case_5(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 5)
        self.assertEqual(result, -1)

    def test_case_6(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 6)
        self.assertEqual(result, 4)

    def test_case_7(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 0)
        self.assertEqual(result, -1)

    def test_case_8(self):
        array = [1, 2, 3, 4, 6]
        result = target.binary_search(array,0, 10)
        self.assertEqual(result, -1)
    
    def test_case_9(self):
        array = [1, 14, 33, 45, 85]
        result = target.binary_search(array,0, 44)
        self.assertEqual(result, -1)
    
    def test_case_10(self):
        array = [1, 14, 33, 45, 85]
        result = target.binary_search(array,0, 33)
        self.assertEqual(result, 2)
    
    def test_case_11(self):
        array = [1, 14, 33, 45, 85]
        result = target.binary_search(array,0, 80)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()