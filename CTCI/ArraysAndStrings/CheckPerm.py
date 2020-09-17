# Given two strings, write a method to decide if one is a permutation of the other.

from BasicHashTable import *

def checkPermutation(string1, string2):
	# base case
	if len(string1) != len(string2):
		return False
	else:
		hashTable = HashTable()
		for character in string1:
			hashTable.insert(character, character)
		for character in string2:
			if hashTable.remove(character) == None:
				return False
		return True

print(checkPermutation("Cat in The Hat", "Hat in The Cat"))
print(checkPermutation("ABCDEFG", "ABCDEFF"))