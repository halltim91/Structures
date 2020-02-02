#Auth Timothy Hall
#Date 2/1/2020
#Desc Implementation of a BST


class node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	#Recursively prints the data and the data of the children nodes in numerical order
	def display(self):
		if self.left is not None:
			self.left.display()
		print(self.data)
		if self.right is not None:
			self.right.display()

class tree:

	def __init__(self):
		self.root = None

	#Wrapper function for recursive _insert()
	def add(self, data):
		self.root = self._insert(self.root, data)
		
	#Prints the tree in numerical order
	def printTreeInOrder(self):
		print("Tree entries:")
		if self.root is None:
			print("Tree is Empty")
		else:
			self.root.display()

	#Returns the height of the tree
	def height(self):
		return self._height(self.root)

	#Returns True if tree is balanced
	def isBalanced(self):
		return self._isBalanced(self.root)

	#Recursively inserts a new node into the tree
	def _insert(self, root, data):
		if root is None:
			root = node(data)
			return root
		else:
			if root.data < data:
				if root.right is None:
					root.right = node(data)
					return root
				else:
					self._insert(root.right, data)
					return root
			else:
				if root.left is None:
					root.left = node(data)
					return root
				else:
					self._insert(root.left, data)
					return root

	#Recursively counts the height of the tree
	def _height(self, root):
		if root is None:
			return 0
		else:
			return max(self._height(root.left), self._height(root.right)) + 1

	#recursively checks if tree is balanced
	def _isBalanced(self, root):
		if root is None:
			return True
		lh = self._height(root.left)
		rh = self._height(root.right)
		if(abs(lh - rh) <= 1) and self._isBalanced(root.left) is True and self._isBalanced(root.right) is True:
			return True
		return False


#Driver program
tree = tree()
tree.add(30)
tree.add(40)
tree.add(20)
tree.add(34)
tree.add(32)
tree.printTreeInOrder()
print("Tree height: " + str(tree.height()))
print("Tree is Balanced: " + str(tree.isBalanced()))
