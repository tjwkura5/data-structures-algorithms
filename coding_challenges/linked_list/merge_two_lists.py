class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1
        return True
   
def merge_two(list1, list2):
    result = []
    my_linked_list = __merge_two(list1, list2)
    if my_linked_list:
        temp = my_linked_list.head
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result
    else:
        return []

def __merge_two(list1, list2):
    if not list1 and not list2:
        return None
    if list1 and not list2:
        my_linked_list = LinkedList(list1[0])
        p1 = 1
        p2 = 0
    if list2 and not list1:
        my_linked_list = LinkedList(list2[0])
        p2 = 1
        p1 = 0
    if list1 and list2:
        if list1[0] < list2[0]:
            my_linked_list = LinkedList(list1[0])
            p1 = 1
            p2 = 0
        else:
            my_linked_list = LinkedList(list2[0])
            p2 = 1
            p1 = 0

    while p1 < len(list1) or p2 < len(list2):
        if p1 < len(list1) and p2 < len(list2):
            if list1[p1] < list2[p2]:
                my_linked_list.append(list1[p1])
                p1 += 1
            else:
                my_linked_list.append(list2[p2])
                p2 +=1
        else:
            if p2 < len(list2):
                my_linked_list.append(list2[p2])
                p2 +=1
            if p1 < len(list1):
                my_linked_list.append(list1[p1])
                p1 += 1
    return my_linked_list

print(merge_two([7,6,8],[1,3,4,5]))
