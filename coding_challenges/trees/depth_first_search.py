class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        if root:
            self.root = TreeNode(root)
        else:
            self.root = root
    
    def insert(self, current_node, value):
        if self.root == None:
            self.root = TreeNode(value)
            return self.root
        if not current_node:
            return TreeNode(value)
        
        if value > current_node.value:
            current_node.right = self.insert(current_node.right, value)
        if value < current_node.value:
            current_node.left = self.insert(current_node.left, value)

        return current_node
    
    # Depth First Search 
    def inorder(self, current_node):
        if not current_node:
            return
        self.inorder(current_node.left)
        print(current_node.value)
        self.inorder(current_node.right)

    def preOrder(self, current_node):
        if not current_node:
            return 
        print(current_node.value)
        self.preOrder(current_node.left)
        self.preOrder(current_node.right)

    def postOrder(self, current_node):
        if not current_node:
            return
        self.postOrder(current_node.left)
        self.postOrder(current_node.right)
        print(current_node.value)

myTree = BinarySearchTree(1)
myTree.insert(myTree.root, 2)
myTree.insert(myTree.root, 3)

myTree.inorder(myTree.root)