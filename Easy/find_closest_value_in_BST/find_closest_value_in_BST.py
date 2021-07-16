class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_closest_value_in_BST(tree, searchedNum):
    
    closest = tree.data
    if abs(searchedNum - tree.data) == 0:
        return tree.data
    if tree.left != None and searchedNum < tree.data:
        closest = find_closest_value_in_BST(tree.left, searchedNum) if abs(searchedNum - find_closest_value_in_BST(tree.left, searchedNum)) < abs(searchedNum - closest) else closest
    if tree.right != None and searchedNum > tree.data:
        closest = find_closest_value_in_BST(tree.right, searchedNum) if abs(searchedNum - find_closest_value_in_BST(tree.right, searchedNum)) < abs(searchedNum - closest) else closest
    return closest
    