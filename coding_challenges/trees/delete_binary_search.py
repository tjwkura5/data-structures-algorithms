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
        if self.root == None:
            self.root = TreeNode(val)
            return self.root
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        return root
    
    def minimum_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value
        

    def _delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)
        else:
            # Deleting a leaf node
            if current_node.left == None and current_node.right == None:
                return None
            # Deleting a node with a right sub tree
            elif current_node.left == None:
                current_node = current_node.right
            #Deleting a node with a left sub tree
            elif current_node.right == None:
                current_node = current_node.left 
            else:
                #Deleting a node with a right and left sub tree 
                sub_tree_min = self.minimum_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self._delete_node(current_node.right, sub_tree_min)

            
            return current_node

    
        # return current_node

    def delete_node(self, value):
        self._delete_node(self.root, value)
