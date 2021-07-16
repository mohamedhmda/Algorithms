import unittest

target = __import__("first_non_repeating_char")

class TestFNRChar(unittest.TestCase):
    def test_case_1(self):
        string = "aabcdd"
        expected_result = "b"
        result = target.first_non_repeating_char(string)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        string = "GeeksforGeeks"
        expected_result = "f"
        result = target.first_non_repeating_char(string)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        string = "wwwwaaadexxxxxxywww"
        expected_result = "d"
        result = target.first_non_repeating_char(string)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()