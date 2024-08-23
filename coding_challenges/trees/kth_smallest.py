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
    
    def inorder(self, current_node, res):
        if not current_node:
            return 
        self.inorder(current_node.left, res)
        res.append(current_node.value)
        self.inorder(current_node.right, res)

    def find_kth_smallest(self, k):
        res = []
        self.inorder(self.root, res)
        return res[k-1]
            
myTree = BinarySearchTree(3)
myTree.insert(myTree.root, 1)
myTree.insert(myTree.root, 4)
myTree.insert(myTree.root, 2)

print(myTree.find_kth_smallest(1))

