class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def kth_smallest(self, k):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if len(results) < k:
                results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        if len(results) == k and len(results) != 0:
            return results[k -1]
        return None
    
    # def kth_smallest(self, k):
    #     stack = []
    #     node = self.root
        
    #     while stack or node:
    #         while node:
    #             stack.append(node)
    #             node = node.left
            
    #         node = stack.pop()
    #         k -= 1
    #         if k == 0:
    #             return node.value
            
    #         node = node.right
            
    #     return None
                



my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.kth_smallest(0))  # Expected output: 2
print(my_tree.kth_smallest(3))  # Expected output: 4
print(my_tree.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """