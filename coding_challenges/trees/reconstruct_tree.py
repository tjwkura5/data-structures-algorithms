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
    
    def re_engineer(self, preOrder, inorder):
        if not preOrder or not inorder:
            return None
        root = TreeNode(preOrder[0])
        mid = inorder.index(preOrder[0])
        root.left = self.re_engineer(preOrder[1:mid+1], inorder[:mid])
        root.right = self.re_engineer(preOrder[mid+1:], inorder[mid + 1])
        return root 