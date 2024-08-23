# Binary Search Trees

# Difference between Binary Trees and Binary Search Trees

# Binary Search Trees (BST) are a variation of binary trees with a sorted property to them. 
# The property tells us that every left child must be smaller than its parent 
# and every right child must be greater than its parent. BSTs do not allow duplicates.

# Motivation

# The question here is why bother with BSTs if we have sorted arrays? 
# With binary search, we can search values in O(log n) time and 
# if BST is offering the same functionality, can't we just use an array? 
# All of this is correct. However, BST shines when we are trying to insert or delete a value. 
# Both of these operations run in O(log n) time for a BST, but O(n)
# time with an array.

# So, while BSTs don't offer benefit over sorted arrays for the search functionality, 
# they are better for insertion and deletion. 
# In this chapter, we will focus specfically on the search operation.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def search(self, root, target):
        if not root:
            return False
        if target > root.val:
            return self.search(root.right, target)
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return True
    
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        return root

    