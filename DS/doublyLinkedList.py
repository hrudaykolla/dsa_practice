class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.main_head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.main_head is None:
            self.main_head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def __str__(self):
        current = self.main_head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next_node
        return f'[none {", ".join(map(str, nodes))} none]'

# Create a doubly linked list
my_list = DoublyLinkedList()

# Add nodes to the list
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)

# # Print the data of the nodes
print(my_list)

