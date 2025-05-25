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
        self.head = header_node
        self.tail = header_node

    def ensure_header_exists(self):
        if self.head is None:
            self.add_header_node()

    def add_node(self, data):
        self.ensure_header_exists()
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node
        self.head.node_count += 1

        if self.head.min_node is None or self.head.min_node > new_node.data:
            self.head.min_node = new_node.data
        if self.head.max_node is None or self.head.max_node < new_node.data:
            self.head.max_node = new_node.data

    def insert_new_node_after_header(self, data):
        self.ensure_header_exists()
        new_node = Node(data)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

        if self.tail == self.head:
            self.tail = new_node  # Fix for empty list after header

        self.head.node_count += 1

        if self.head.min_node is None or self.head.min_node > new_node.data:
            self.head.min_node = new_node.data
        if self.head.max_node is None or self.head.max_node < new_node.data:
            self.head.max_node = new_node.data

    def display(self):
        current = self.head
        while current is not None:
            if current == self.head:
                print(f'Header Node:')
                print(f'  Node count: {self.head.node_count}')
                print(f'  Max value: {self.head.max_node}')
                print(f'  Min value: {self.head.min_node}')
                print('List:', end=' ')
                current = current.next_node
            else:
                print(current.data, end=" -> ")
                current = current.next_node
        print("Tail(None)")


if __name__ == "__main__":
    my_list = HeaderLinkedList()

    # Add nodes to the list
    my_list.add_node(2)
    my_list.add_node(3)
    my_list.add_node(4)
    my_list.add_node(5)

    # Display the list
    my_list.display()

    # Insert a new node right after the header
    my_list.insert_new_node_after_header(1)

    # Display again
    my_list.display()
