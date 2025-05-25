class Node:
    def __init__(self, value):
        self.data = value
        self.prev_node = None
        self.next_node = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def enqueue(self,data):
        new_node = Node(data)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail = new_node
            new_node.prev_node.next_node = self.tail

    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            self.length -= 1
            self.head = self.head.next_node

    def display(self):
        print(f'queue from start to end')
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
    
    def len(self):
        return self.length

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    print(f"queue length: {my_queue.length}")

    my_queue.display()

    my_queue.dequeue()

    my_queue.display()
    print(f"queue lenght: {my_queue.len()}")

