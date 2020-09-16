# Implement an algorithm to determine if a string has all unique characters.
# What if you cannont use any additional data structures?

from BasicHashTable import *

def IsUnique(string):
	hashTable = HashTable()
	for character in string:
		if hashTable.find(character) == character:
			return False
		else:
			hashTable.insert(character, character)
	return True

print(IsUnique("abcdefghijjk"))