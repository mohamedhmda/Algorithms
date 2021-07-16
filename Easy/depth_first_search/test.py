import unittest

target = __import__("depth_first_search")

class TestNodeDepths(unittest.TestCase):
    def setUp(self):
        # level 1
        self.tree = target.Node(1)
        # level 2
        self.tree.left = target.Node(2)
        self.tree.right = target.Node(3)
        # level 3
        self.tree.left.left = target.Node(4)
        self.tree.left.right = target.Node(5)

    def test_case_1(self):
        result = target.depth_first_search(self.tree)
        self.assertEqual(result, [4, 2, 5, 1, 3])
    
if __name__ == "__main__":
    unittest.main()