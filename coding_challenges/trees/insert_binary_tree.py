class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root = None):
        if root:
            self.root = TreeNode(root)
        else:
            self.root = root

    def insert(self, root, value):
        node = TreeNode(value)
        if self.root == None:
            self.root = node
            return node
        
        if not root:
            return node 
        
        if root.value > value:
            root.left = self.insert(root.left, value)
        elif root.value < value:
            root.right = self.insert(root.right, value)

        return root
    

myTree = BinarySearchTree(4)
myTree.insert(myTree.root, 2)
myTree.insert(myTree.root, 7)
myTree.insert(myTree.root, 1)
print(myTree.insert(myTree.root, 3).value)


