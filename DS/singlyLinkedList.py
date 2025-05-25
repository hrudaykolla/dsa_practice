class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
    
    def insert_new_node_after_head(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search_node(self, data):
        current = self.head
        count = 1
        while current is not None:
            if current.data == data: return count
            else: count += 1
            current = current.next_node
        return -1
    
    def insert_new_node_after_node(self,data, node):
        new_node = Node(data)
        node_position = self.search_node(node)
        current = self.head
        current_node_position = 1
        if node_position >= 1:
            while (node_position-current_node_position) > 0:
                current = current.next_node
                current_node_position += 1
            new_node.next_node = current.next_node
            current.next_node = new_node

    def insert_new_node_at_pos(self,data, node_pos):
        new_node = Node(data)
        current = self.head
        current_node_position = 1
        while (node_pos - current_node_position) > 1:
            current = current.next_node
            current_node_position += 1
        new_node.next_node = current.next_node
        current.next_node = new_node
    
    def delete_node_at_pos(self, node_pos):
        current = self.head
        current_node_position = 1
        while (node_pos - current_node_position) > 1:
            current = current.next_node
            current_node_position += 1
        current.next_node = current.next_node.next_node
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next_node
        print("Tail(None)")

# Create a singly linked list
my_list = SinglyLinkedList()

# Add nodes to the list
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(5)

# Display the list
my_list.display()

my_list.insert_new_node_after_head(1)
my_list.display()

print(my_list.search_node(3))

my_list.insert_new_node_after_node(4,3)
my_list.display()

my_list.insert_new_node_at_pos(6,6)
my_list.display()

my_list.delete_node_at_pos(3)
my_list.display()