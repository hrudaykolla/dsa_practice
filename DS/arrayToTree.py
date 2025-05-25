
from Queue import Queue

class treeNode:
    def __init__(self,data):
        self.data = data
        self.left_node = None
        self.right_node = None

class arrayToTree:
    def __init__(self):
        self.root = None
        self.my_queue_nodes = Queue()
    
    def minTree(self,array):
        array.sort()
        for element in array:
            # print(element)
            new_node = treeNode(element)

            if self.root is None:
                self.root = new_node
                self.my_queue_nodes.enqueue(self.root)
            
            elif self.my_queue_nodes.head.data.left_node is None:
                self.my_queue_nodes.head.data.left_node = new_node
                self.my_queue_nodes.enqueue(self.my_queue_nodes.head.data.left_node)

            elif self.my_queue_nodes.head.data.right_node is None:
                self.my_queue_nodes.head.data.right_node = new_node
                self.my_queue_nodes.enqueue(self.my_queue_nodes.head.data.right_node)

            if self.my_queue_nodes.head.data.left_node is not None and self.my_queue_nodes.head.data.right_node is not None:
                self.my_queue_nodes.dequeue()
    
    def maxTree(self,array):
        array.sort()
        array.reverse()
        for element in array:
            # print(element)
            new_node = treeNode(element)

            if self.root is None:
                self.root = new_node
                self.my_queue_nodes.enqueue(self.root)
            
            elif self.my_queue_nodes.head.data.left_node is None:
                self.my_queue_nodes.head.data.left_node = new_node
                self.my_queue_nodes.enqueue(self.my_queue_nodes.head.data.left_node)

            elif self.my_queue_nodes.head.data.right_node is None:
                self.my_queue_nodes.head.data.right_node = new_node
                self.my_queue_nodes.enqueue(self.my_queue_nodes.head.data.right_node)

            if self.my_queue_nodes.head.data.left_node is not None and self.my_queue_nodes.head.data.right_node is not None:
                self.my_queue_nodes.dequeue()
        
    # def display(sarrayToTree
    #     current_node = self.root
    #     while current_node is not None:
    #         print(current_node.data)
    #         current_node = current_node.left_node
        
                
my_array_to_heap = arrayToTree()
my_array_to_heap.maxTree([1,2,3,4,5,6,7])

print(my_array_to_heap.root.data)
print(my_array_to_heap.root.left_node.data) 
print(my_array_to_heap.root.right_node.data)

print(my_array_to_heap.root.left_node.left_node.data)
print(my_array_to_heap.root.left_node.right_node.data)

print(my_array_to_heap.root.right_node.left_node.data)
print(my_array_to_heap.root.right_node.right_node.data)

# [1,2,3,4,5,6,7]
# n = 7
# L = math.ceil(math.log2(n+1)-1)
# print(L)
""" 
            1
    2               3
4       5       6       7
"""
