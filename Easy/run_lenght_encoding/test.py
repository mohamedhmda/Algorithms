import unittest

target = __import__('run_lenght_encoding')

class TestRunLenghtEncoding(unittest.TestCase):
    def test_case_1(self):
        string = "wwwwaaadexxxxxx"
        new_string = "w4a3d1e1x6"
        result = target.run_lenght_encoding(string)
        self.assertEqual(result, new_string)

    def test_case_2(self):
        string = "abcd"
        new_string = "a1b1c1d1"
        result = target.run_lenght_encoding(string)
        self.assertEqual(result, new_string)

    def test_case_3(self):
        string = "wwwwaaadexxxxxxywww"
        new_string = "w4a3d1e1x6y1w3"
        result = target.run_lenght_encoding(string)
        self.assertEqual(result, new_string)
    

if __name__ == '__main__':
    unittest.main()
