#Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

#An array is said to be monotonic if its elements, from left to right, are entirely non-increaing or entirely non-decreasing.

#Non-increasing elements aren't necessarily exclusively decreasing; they simply do not increase, and vice versa. Empty array and arrays of one element are monotonic.

#the solution below is slightly difficult to follow and does not feel very intuitive. I believe this approach works better if the question was worded as such: assume you have an array of DISTINCT integers, determine whether the array is strictly decreasing or strictly increasing. In that case, this solution works well. if their may be duplicate values, solution #2 is a better approach.

#O(n) time | O(1) space
def isMonotonic(array):
	if len(array) <= 2:
		return True
	
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if breaksDirection(direction, array[i - 1], array[i]):
			return False
	return True

def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	if direction > 0:
		return difference < 0
	return difference > 0

#the solution below feels more intuitive and less error prone. Essentially were approaching the problem to determine whether the array is constantly non decreasing or constantly non increasing. we have a for loop that iterates through the array starting at index 1, checking to see if the current index is greater than or equal to the previous index. we know if the current index is less than the previous index, then the array is decreasing, so we set isNonDescreasing to false. if the current index is greater than the prevous index, then we know that the array increasing, so we set isNonIncreasing to false. we know that if either one of those variables is returned, or both (meaning that each index in the array is the same), then the array is monotonic.

#O(n) time | O(1) space
def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			isNonDecreasing = False
		if array[i] > array[i - 1]:
			isNonIncreasing = False
			
	return isNonDecreasing or isNonIncreasing
	