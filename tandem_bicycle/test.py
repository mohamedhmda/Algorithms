import unittest

target = __import__("tandem_bicycle")

class TestTandemBicycle(unittest.TestCase):
    def test_case_1(self):
        blue_drivers = [8, 5, 3]
        red_drivers = [7, 2, 4]
        result = target.tandem_bicycle(blue_drivers, red_drivers, True)
        self.assertEqual(result, 20)

    def test_case_2(self):
        blue_drivers = [8, 5, 3]
        red_drivers = [7, 2, 4]
        result = target.tandem_bicycle(blue_drivers, red_drivers, False)
        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()