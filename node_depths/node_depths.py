class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def node_depths(tree, prev_depth):
    depth = prev_depth
    if tree.left != None:
        depth = depth + node_depths(tree.left, prev_depth+1)
    if tree.right != None:
        depth = depth + node_depths(tree.right, prev_depth+1)
    return depth