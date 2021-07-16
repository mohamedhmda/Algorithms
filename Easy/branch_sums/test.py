import unittest

target = __import__("branch_sums")

class TestBranchSums(unittest.TestCase):
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
        # level 4
        self.tree.left.left.left = target.Node(8)
        self.tree.left.left.right = target.Node(9)

    def test_case_1(self):
        result = target.branch_sums(self.tree)
        sums = [15, 16, 8, 10, 11]
        self.assertEqual(result, sums)

if __name__ == '__main__':
    unittest.main()