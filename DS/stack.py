class Node:
    def __init__(self, data):
        self.data = data
        self.next_down_node = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_down_node = self.top
            self.top = new_node

    def pop(self):
        if self.top is not None:
            self.top = self.top.next_down_node
        # elif self.top is not None and self.top.next_down_node is None:
        #     self.top = self.top.next_down_node
        
    
    # def search_node(self, data):
    #     current = self.head
    #     count = 1
    #     while current is not None:
    #         if current.data == data: return count
    #         else: count += 1
    #         current = current.next_node
    #     return -1
        
    def display(self):
        current = self.top
        while current is not None:
            print(f'{current.data}')
            current = current.next_down_node
        # print("(None)")
        


my_stack = Stack()

my_stack.push(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print(my_stack.display())

my_stack.pop()
print(my_stack.display())
my_stack.pop()
print(my_stack.display())
my_stack.pop()
print(my_stack.display())
my_stack.pop()
print(my_stack.display())

my_stack.push(1)
print(my_stack.display())

my_stack.push(2)
print(my_stack.display())