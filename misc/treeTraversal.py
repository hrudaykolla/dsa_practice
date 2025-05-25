# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A function to do inorder tree traversal
def printInorder(root):

	if root:
		printInorder(root.left) # First recur on left child
		print(root.val, end=" ") # Then print the data of node
		printInorder(root.right) # Now recur on right child

# A function to do preorder tree traversal
def printPreorder(root):
 
    if root: 
        print(root.val, end=" ") # First print the data of node
        printPreorder(root.left) # Then recur on left child
        printPreorder(root.right) # Finally recur on right child

# A function to do postorder tree traversal
def printPostorder(root):
	if root:
		printPostorder(root.left) # First recur on left child
		printPostorder(root.right) # The recur on right child
		print(root.val, end=" ") # Now print the data of node

# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	# Function call
	print(f"Inorder traversal of binary tree is")
	printInorder(root)

	print(f"\nPreorder traversal of binary tree is")
	printPreorder(root)

	print(f"\nPostorder traversal of binary tree is")
	printPostorder(root)

