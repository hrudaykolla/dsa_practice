# Circular Linked List: each node has details about its data and next node.
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
            self.tail.next_node = self.head

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next_node
        print("Tail(None)")

if __name__ == "__main__":
    # Create a singly linked list
    my_list = SinglyLinkedList()

    # Add nodes to the list
    my_list.add_node(1)
    my_list.add_node(2)
    my_list.add_node(3)

    # Display the list
    my_list.display()


    print(my_list.head.next_node.data)
    print(my_list.tail.data)