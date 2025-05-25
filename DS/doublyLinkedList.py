class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
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
            new_node.prev_node = self.tail
            self.tail = new_node

    def __str__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next_node
        return " <-> ".join(["None"] + list(map(str, nodes)) + ["None"])

if __name__ == "__main__":
    # Create a doubly linked list and add nodes
    my_list = DoublyLinkedList()
    my_list.add_node(1)
    my_list.add_node(2)
    my_list.add_node(3)

    # Print the list
    print(my_list)  # Output: None <-> 1 <-> 2 <-> 3 <-> None


