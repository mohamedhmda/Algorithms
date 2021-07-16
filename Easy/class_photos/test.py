import unittest

target = __import__("class_photos")

class TestClassPhotos(unittest.TestCase):
    def test_case_1(self):
        red_row = [3,5,4]
        blue_row = [2,3,1]

        result = target.class_photos(red_row, blue_row)
        self.assertTrue(result)

    def test_case_2(self):
        red_row = [3,5,4]
        blue_row = [2,3,6]

        result = target.class_photos(red_row, blue_row)
        self.assertFalse(result)

    def test_case_3(self):
        red_row = [3,5,4]
        blue_row = [2,3,6]

        result = target.class_photos(red_row, blue_row)
        self.assertFalse(result)

    def test_case_4(self):
        red_row = [4, 6, 2, 7]
        blue_row = [3, 5, 8, 9]

        result = target.class_photos(red_row, blue_row)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()