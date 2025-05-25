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
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.head is None:
            print("Queue is Empty")
            return None
        removed_data = self.head.data
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        else:
            self.tail = None  # Queue is now empty
        self.length -= 1
        return removed_data

    def display(self):
        print('Queue from start to end:')
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def len(self):
        return self.length

    def search(self, value):
        current_node = self.head
        position = 0
        while current_node is not None:
            if current_node.data == value:
                return position
            current_node = current_node.next_node
            position += 1
        return -1  # Not found

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    print(f"Queue length: {my_queue.len()}")

    my_queue.display()

    print(f"\nDequeued: {my_queue.dequeue()}")
    my_queue.display()
    print(f"Queue length: {my_queue.len()}")

    search_val = 3
    index = my_queue.search(search_val)
    if index != -1:
        print(f"Value {search_val} found at position {index}")
    else:
        print(f"Value {search_val} not found in queue")
