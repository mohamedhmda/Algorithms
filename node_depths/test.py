import unittest

target = __import__("node_depths")

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
        self.tree.right.left = target.Node(6)
        self.tree.right.right = target.Node(7)

    def test_case_1(self):
        result = target.node_depths(self.tree, 0)
        self.assertEqual(result, 10)
    
if __name__ == "__main__":
    unittest.main()