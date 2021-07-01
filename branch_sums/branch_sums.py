class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def calculate_branch_sums(tree, prev_sum, sums):
    prev_sum +=  tree.data

    if tree.left is None and tree.right is None:
        return sums.append(prev_sum)

    if tree.left != None:
        calculate_branch_sums(tree.left, prev_sum, sums)

    if tree.right != None:
        calculate_branch_sums(tree.right, prev_sum, sums)

def branch_sums(tree):
    sums = []
    calculate_branch_sums(tree, 0, sums)
    return sums
