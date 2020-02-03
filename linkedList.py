#Auth Timothy Hall
#Date 2/2/2020
#Desc Implementation of Linked Lists

class node:

	def __init__(self, data):
		self.data = data
		self.next = None

	#Recursively print the items in the list
	def print(self):
		print(self.data)
		if self.next is not None:
			self.next.print()


class linkedList:

	def __init__(self):
		self.head = None
		self.tail = self.head

	#Push an item to the front of the list
	def push(self, data):
		if self.head is None:
			self.head = node(data)
			self.tail = self.head
		else:
			temp = node(data)
			temp.next = self.head
			self.head = temp

	#Manualy travers the list to append item using recursion
	def _append(self, n, data):
		if n is None:
			n = node(data)
			# still need to update pointer incase append2 is called
			self.tail = n 
			return n
		else:
			n.next = self._append(n.next, data)
			return n
	
	#using Recursive method
	def append(self, data):
		self.head = self._append(self.head, data)

	#append list using tail pointer
	def append2(self, data):
		temp = node(data)
		self.tail.next = temp
		self.tail = self.tail.next

	#Prints out data in each node
	def print(self):
		if self.head is None:
			print("List is Empty")
		else:
			self.head.print()

	#Emulate manually freeing memory
	def _clear(self, n):
		if n is None:
			return n
		n.next = self._clear(n.next)
		n = None
		return n

	#Empties the List
	def clear(self):
		self.head = self._clear(self.head)


#Driver program to test Functions

list = linkedList()
print("Pushing items to front of list")
list.push(3)
list.push(4)
list.push(5)
list.push(67)
list.print()

print("Appending items to end of the list")
list.append(10)
list.append(3)
list.append(4)
list.append(8)
list.append2(32)
list.append2(100)
list.print()

print("Clearing List")
list.clear()
list.print()