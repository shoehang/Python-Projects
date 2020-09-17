# linked list approach hashing; chaining to avoid collisions
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

class HashTable:
	def __init__(self):
		self.capacity = 100
		self.size = 0
		self.buckets = [None] * self.capacity

	# rolling polynomial hashing for strings
	# P: The value of P can be any prime number roughly equal to the number of different characters used. 
	# For example: if the input string contains only lowercase letters of the English alphabet, then P = 31 is the appropriate value of P. 
	# If the input string contains both uppercase and lowercase letters, then P = 53 is an appropriate option.
	# M: the probability of two random strings colliding is inversely proportional to m, Hence m should be a large prime number. 
	# M = 10 ^9 + 9 is a good choice.
	# geeksforgeeks
	def hash(self, key):
		p = 53
		m = 1e9 + 9
		power_p = 1
		hash_val = 0
		for i in range(len(key)):
			hash_val = ((hash_val + (ord(key[i]) - ord('a') + 1) * power_p) % m)
			power_p = (power_p * p) % m
		hash_val = hash_val % self.capacity
		'''
		hashResult = 0
		for index, character in enumerate(key):
			# some random hash function
			hashResult += (index ** ord(character)) + len(key)
			# keeps result in range of buckets
			hashResult = hashResult % 100
		'''
		return int(hash_val)

	def insert(self, key, value):
		self.size += 1
		index = self.hash(key)
		node = self.buckets[index]
		# empty bucket insert
		if node is None:
			self.buckets[index] = Node(key, value)
			return
		# occupied bucket insert
		else:
			# find end of linked list and insert new node
			previous = node
			while node is not None:
				previous = node
				node = node.next
			previous.next = Node(key, value)
			return

	def remove(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		previous = None
		while node is not None and node.key != key:
			previous = node
			node = node.next
		# not found
		if node == None:
			return None
		# found
		else:
			self.size -= 1
			found = node.value
			if previous == None:
				if node.next == None:
					self.buckets[index] = None
				else:
					previous = node.next
					node.next = None
					self.buckets[index] = previous
					node = None
			else:
				# same removal in normal linked lists
				previous.next = previous.next.next
			return found

	def find(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return None
		else:
			return node.value