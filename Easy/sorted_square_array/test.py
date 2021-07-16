import unittest
from unittest.case import TestCase

target = __import__("sorted_square_array")

class TestSortedSquareArrayWithSort(unittest.TestCase):
    def test_case_1(self):
        array = [-1, 2, 5, -6, 3]
        sorted_array = [1, 4, 9, 25, 36]
        result = target.sorted_square_array_with_sort(array)
        self.assertEqual(result, sorted_array)

    def test_case_2(self):
        array = [-4,-1,0,3,10]
        sorted_array = [0,1,9,16,100]
        result = target.sorted_square_array_with_sort(array)
        self.assertEqual(result, sorted_array)
    
    def test_case_3(self):
        array = [-7,-3,2,3,11]
        sorted_array = [4,9,9,49,121]
        result = target.sorted_square_array_with_sort(array)
        self.assertEqual(result, sorted_array)



class TestSortedSquareArray(unittest.TestCase):
    def test_case_1(self):
        array = [-1, 2, 5, -6, 3]
        sorted_array = [1, 4, 9, 25, 36]
        result = target.sorted_square_array(array)
        self.assertEqual(result, sorted_array)

    def test_case_2(self):
        array = [-4,-1,0,3,10]
        sorted_array = [0,1,9,16,100]
        result = target.sorted_square_array(array)
        self.assertEqual(result, sorted_array)
    
    def test_case_3(self):
        array = [-7,-3,2,3,11]
        sorted_array = [4,9,9,49,121]
        result = target.sorted_square_array(array)
        self.assertEqual(result, sorted_array)

if __name__ == '__main__':
    unittest.main()