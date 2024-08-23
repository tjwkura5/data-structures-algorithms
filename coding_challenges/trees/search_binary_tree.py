# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and 
# return the subtree rooted with that node. If such a node does not exist, return null.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, node, target):
        if not node:
            return []
        if target > node.value:
            return self.search(node.right, target)
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return [target, node.left.value, node.right.value]

# Input: root = [4,2,7,1,3], val = 2

# Input: root = [4,2,7,1,3], val = 5
