import unittest

target = __import__("find_closest_value_in_BST")

class TestFindClosestValueInBST(unittest.TestCase):
    def setUp(self):
        self.tree = target.Node(9)

        self.tree.left = target.Node(4)
        self.tree.right = target.Node(17)

        self.tree.left.left = target.Node(3)
        self.tree.left.right = target.Node(6)
        self.tree.right.right = target.Node(22)

        self.tree.left.right.left = target.Node(5)
        self.tree.left.right.right = target.Node(7)

        self.tree.right.right.left = target.Node(20)

    def test_case_1(self):
        result = target.find_closest_value_in_BST(self.tree, 4)
        self.assertEqual(result, 4)

    def test_case_2(self):
        result = target.find_closest_value_in_BST(self.tree, 18)
        self.assertEqual(result, 17)

    def test_case_3(self):
        result = target.find_closest_value_in_BST(self.tree, 12)
        self.assertEqual(result, 9)

    def test_case_4(self):
        result = target.find_closest_value_in_BST(self.tree, 50)
        self.assertEqual(result, 22)


if __name__ == "__main__":
    unittest.main()