import unittest

target = __import__("caesar_cipher")

class TestCaesarCipher(unittest.TestCase):
    def test_case_1(self):
        message = "AAA"
        key = 1
        cypher = "BBB"
        result = target.caesar_cipher(message, key)
        self.assertEqual(result, cypher)

    def test_case_2(self):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = 23
        cypher = "XYZABCDEFGHIJKLMNOPQRSTUVW"
        result = target.caesar_cipher(message, key)
        self.assertEqual(result, cypher)

    def test_case_3(self):
        message = "ATTACKATONCE"
        key = 4
        cypher = "EXXEGOEXSRGI"
        result = target.caesar_cipher(message, key)
        self.assertEqual(result, cypher)

if __name__ == "__main__":
    unittest.main()