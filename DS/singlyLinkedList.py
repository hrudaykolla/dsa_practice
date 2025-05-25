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
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def insert_node_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_new_node_after_node(self, data, node_data):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if current.data == node_data:
                new_node.next_node = current.next_node
                current.next_node = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next_node
        print(f"Node with data {node_data} not found.")

    def insert_new_node_at_pos(self, data, node_pos):
        new_node = Node(data)
        if node_pos <= 0:
            raise IndexError("Position must be >= 1")
        if node_pos == 1:
            self.insert_node_at_head(data)
            return
        current = self.head
        current_pos = 1
        while current and current_pos < node_pos - 1:
            current = current.next_node
            current_pos += 1
        if current is None:
            raise IndexError("Position out of bounds")
        new_node.next_node = current.next_node
        current.next_node = new_node
        if new_node.next_node is None:
            self.tail = new_node

    def delete_node_at_pos(self, node_pos):
        if node_pos <= 0:
            raise IndexError("Position must be >= 1")
        if self.head is None:
            print("List is empty.")
            return
        if node_pos == 1:
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return
        current = self.head
        current_pos = 1
        while current.next_node and current_pos < node_pos - 1:
            current = current.next_node
            current_pos += 1
        if current.next_node is None:
            raise IndexError("Position out of bounds")
        if current.next_node == self.tail:
            self.tail = current
        current.next_node = current.next_node.next_node

    def search_node(self, data):
        current = self.head
        position = 1
        while current:
            if current.data == data:
                return position
            current = current.next_node
            position += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print("Tail(None)")


# Test the list
if __name__ == "__main__":
    my_list = SinglyLinkedList()

    my_list.add_node(2)
    my_list.add_node(3)
    my_list.add_node(5)
    my_list.display()

    my_list.insert_node_at_head(1)
    my_list.display()

    print("Position of node with data 3:", my_list.search_node(3))

    my_list.insert_new_node_after_node(4, 3)
    my_list.display()

    my_list.insert_new_node_at_pos(6, 6)
    my_list.display()

    my_list.delete_node_at_pos(3)
    my_list.display()
