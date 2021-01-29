#You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array. The function should perform this in place by mutating the given array, and doesnt need to maintain the order of the other integers.

#You could sort the array, but that would give you a O(n log n) time complexity. In order to perform in O(n) time, you can use two pointers. One pointer to the left starting at the first index, and one to the right pointing at the last index. You can them use two while loops, the first while will test to see if the left pointer is still to the left of the right pointer (once the pointers cross you know you have traversed the whole array). the reason we check for this again in the nested while is to handle certain edge cases.if this way your input array [2, 1, 2, 2, 2, 3, 4, 2], youre return statement would be [4, 1, 2, 3, 2, 2, 2, 2]. thats because in the last iteration the condition that is checking if array[j] is == toMove would be true if the and statement wasn't there, and would swap the positions before hitting the outer while loop and breaking.




#O(n) time | O(1) space
def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) - 1
	while i < j:
		while array[j] == toMove and i < j:
			j -= 1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array