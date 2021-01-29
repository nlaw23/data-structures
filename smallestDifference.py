#Write a function that takes in two non-empty arrays of integers, finds the pair of numbers(one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position. You can assume that there will only be one pair of numbers with the smallest difference.

#essentially were trying to find a pair of numbers, one from each array, who are closest to each other. if we sort both arrays in place, using an optimal sorting algorithm like quick or merge sort, we can do so in n log n time and m log m time. we could make copies if we did not sort them in place using additional space. ( which would be O(n) ). after we sort both arrays, we set up pointers, one on each array starting at index 0. we declare two variables, one called smallest and one called current, and set them both equal to infinity. the current variable allows us to store the current pair that we just iterated through. the smallest variable allows us to compare the current to the previously smallest calculated difference. for the first iteration, we know smallest will be greater than current because it is set to infinity, in which case we set them equal to each other. for each iteration after, smallest will only get updated if the current variable is less than, meaning it is the new smallest difference. the smallestPair array is set to empty and populated with the firstNum and secondNum that make up the smallest difference. this while loop will run until it tries each value for both arrays.

#O(n log n) + m log (m) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else: 
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair

smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])