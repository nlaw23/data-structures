#write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. if any two numbers in the input array sum up to the target sum, the function should return them in an array in any order. if no two numbers sum up to the target sum, the function should return an empyty array.

#note that the target sum has to be obtained by summing two different integers in the array; you cant add a single integer to itself in order to obtain the target sum.

#you can assume that there will be at most one pair of numbers summing up to the target sum.



# this approach gives you an O(n) time and space complexity. two nested for loops would give you O(n^2) time, with constant space. you could use a sorted array to achieve an O(n log n) runtime with constant space.
def twoNumberSum(array, targetSum):
    nums = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
			nums[num] = True
	return []
	
twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)