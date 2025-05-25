# Stack follows Last In First Out (LIFO)
class Node:
    def __init__(self, data):
        self.data = data
        self.next_down_node = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_down_node = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty. Nothing to pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next_down_node
        return popped_data

    def search(self, data):
        current = self.top
        position = 1
        while current is not None:
            if current.data == data:
                return position
            current = current.next_down_node
            position += 1
        return -1  # Not found
    
    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty.")
            return
        while current:
            print(current.data)
            current = current.next_down_node

if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(4)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)

    my_stack.display()
    print("---")
    print("Search 3:", my_stack.search(3))  # Should print 3
    print("Search 5:", my_stack.search(5))  # Should print -1
    print("---")

    my_stack.pop()
    my_stack.display()
    print("---")

    my_stack.pop()
    my_stack.display()
    print("---")

    my_stack.pop()
    my_stack.display()
    print("---")

    my_stack.pop()
    my_stack.display()
    print("---")

    my_stack.push(1)
    my_stack.display()
    print("---")

    my_stack.push(2)
    my_stack.display()
