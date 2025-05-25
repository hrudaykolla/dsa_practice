#contains node count and max and min value of nodes
class HeaderNode:
    def __init__(self):
        self.node_count = 0
        self.min_node = None
        self.max_node = None
        self.next_node = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class HeaderLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_header_node(self):
        header_node = HeaderNode()
        if self.head is None:
            self.head = header_node
            self.tail = header_node

    def add_node(self, data):
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node
        self.head.node_count += 1
        if  self.head.min_node is None or self.head.min_node > new_node.data:
            self.head.min_node = new_node.data
        if  self.head.max_node is None or self.head.max_node < new_node.data:
            self.head.max_node = new_node.data
    
    def insert_new_node_after_header(self,data):
        new_node = Node(data)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node
        self.head.node_count += 1
        if  self.head.min_node is None or self.head.min_node > new_node.data:
            self.head.min_node = new_node.data
        if  self.head.max_node is None or self.head.max_node < new_node.data:
            self.head.max_node = new_node.data

    def display(self):
        current = self.head
        while current is not None:
            if current == self.head:
                print(f'Node count: {self.head.node_count}')
                print(f'max Node: {self.head.max_node}')
                print(f'min Node: {self.head.min_node}')
                current = current.next_node
            else:   
                print(current.data, end=" -> ")
                current = current.next_node
        print("Tail(None)")

# Create a singly linked list
my_list = HeaderLinkedList()

# Add nodes to the list
my_list.add_header_node()
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)
my_list.add_node(5)
# # Display the list
my_list.display()

my_list.insert_new_node_after_header(1)
my_list.display()

# print(my_list.head.node_count)
# print(my_list.head.max_node)
# print(my_list.head.min_node)
# print(my_list.head.next_node.data)
# print(my_list.head.next_node.next_node.data)
