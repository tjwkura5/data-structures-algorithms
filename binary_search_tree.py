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
        else:
            temp = self.root
            while(True):
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

    def contains(self,value):
        temp = self.root
        while(temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.rigt, value)
        return current_node
    
    def __r_contains(self, current_node, value):
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
        return False

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None 
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
           if current_node.left == None and current_node.right == None:
               return None
           elif current_node.left == None:
               current_node = current_node.right
           elif current_node.right == None:
               current_node = current_node.left
           else:
               sub_tree_min = self.min_value(current_node.right)
               current_node.value = sub_tree_min
               current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def r_contains(self, value):
        self.__r_contains(self.root, value)

    def r_insert(self, value):
        if self.root is None:
          self.root = Node(value)
          return self.root
        return self.__r_insert(self.root, value)
        
    def r_delete(self, value):
        return self.__delete_node(self.root, value)
                
                



my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

my_tree_contains = BinarySearchTree()
my_tree_contains.insert(47)
my_tree_contains.insert(21)
my_tree_contains.insert(76)
my_tree_contains.insert(18)
my_tree_contains.insert(27)
my_tree_contains.insert(52)
my_tree_contains.insert(82)

print(my_tree_contains.contains(27))
print(my_tree_contains.contains(17))