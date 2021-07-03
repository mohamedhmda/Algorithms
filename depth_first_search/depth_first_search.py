class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def calculate_depth_first_search(tree, array):
    if tree.left != None:
        calculate_depth_first_search(tree.left, array)
    array.append(tree.data)
    if tree.right != None:
        calculate_depth_first_search(tree.right, array)

def depth_first_search(tree):
    array = []
    calculate_depth_first_search(tree, array)
    return array
