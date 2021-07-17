import unittest

target = __import__('river_size')

class TestRiverSizes(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ]
        result = target.river_size(matrix)
        expected_result = [2, 1, 5, 2, 2]
        self.assertListEqual(result, expected_result)

    def test_case_2(self):
        matrix = [
            [0],
        ]
        result = target.river_size(matrix)
        expected_result = []
        self.assertListEqual(result, expected_result)
    
    def test_case_3(self):
        matrix = [
            [1],
        ]
        result = target.river_size(matrix)
        expected_result = [1]
        self.assertListEqual(result, expected_result)
    
    def test_case_4(self):
        matrix = [
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
        ]
        result = target.river_size(matrix)
        expected_result = [3, 2, 1]
        self.assertListEqual(result, expected_result)

    def test_case_5(self):
        matrix = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
        ]
        result = target.river_size(matrix)
        expected_result = [2, 1, 21, 5, 2, 1]
        self.assertListEqual(result, expected_result)

    def test_case_6(self):
        matrix = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1]
        ]
        result = target.river_size(matrix)
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertListEqual(result, expected_result)

if __name__=='__main__':
    unittest.main()