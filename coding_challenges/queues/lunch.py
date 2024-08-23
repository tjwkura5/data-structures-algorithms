# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        next = self.head.next
        self.head.next = None
        self.head = next
        self.length -= 1
        return temp.value 

def create_que(students):
    student_que = Queue()
    for student in students:
        student_que.append(student)
    return student_que

def count_students(students, sandwiches):
    student_que = create_que(students)
    curr = student_que.head
    initial = student_que.length
    iterations = 0
    while curr and iterations < initial:
        if curr.value == sandwiches[0]:
            curr = curr.next
            student_que.pop_first()
            sandwiches.pop(0)
        else:
            curr = curr.next
            student_que.append(student_que.pop_first())
            iterations += 1
    return len(sandwiches)

print(count_students([1,1,1,0,0,1], [1,0,0,0,1,1]))