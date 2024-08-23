from collections import deque
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

    def bfs(self, root):
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            print("level: ", level)
            for _ in range(len(queue)):
                curr = queue.popleft()
                print(curr.value)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    