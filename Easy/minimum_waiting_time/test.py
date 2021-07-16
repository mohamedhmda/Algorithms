import unittest

target = __import__("minimum_waiting_time")

class TestMinWaitingTime(unittest.TestCase):
    def test_case_1(self):
        queries = [8, 9, 10, 11]
        result = target.minimum_waiting_time(queries)
        self.assertEqual(result, 52)

    def test_case_2(self):
        queries = [1, 3, 2]
        result = target.minimum_waiting_time(queries)
        self.assertEqual(result, 4)

    def test_case_3(self):
        queries = [3, 5, 1]
        result = target.minimum_waiting_time(queries)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()