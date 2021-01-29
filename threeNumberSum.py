#write a function that takes in a non empty array of distinct integers and an integer representing a target sum. the function should find all triplets in the array that sum up to the target sum and return a two dimensional array of all these triplets. the numbers in each triplt should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. if no three numbers sum up to the target sum, the function should return an empty array.

#naive solution would be three for loops. that would be n^3 time. this below uses n^2 time. we start off by sorting the array. we declare an array that will hold our triplet value(s) that add up to the targetSum. we have a for loop that loops through ( the -2 is because their has to be at least 3 numbers). we assign a left pointer that starts at the next number after current index in the for loop. the right pointer starts at the last element in the array, which is the length of the array - 1. the while loop runs on the condition that the left pointer is less than the right, because if the right is less than, then that means the pointers crossed each other which means we went through every iteration. we declare the currentSum variable to hold the sum of the current indices. if this sum is equal to our targetSum, then we append those values to our triplets array and continue the loop because their could be more than one set of triplets that add up to the targetSum. We increment both pointers at the same time because we know if we do not, that the currentSum will either be too small or too large. we know if the currentSum is less than the targetSum, than we must increment the left pointer in the sorted array, because this will result in the currentSum being increased. we do the opposite of the currentSum is larger than the targetSum. we reutnr triplets once we have looped through all iterations.

#O(n^2) time. O(n) space.
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
	    left = i + 1
	    right = len(array) - 1
	    while left < right:
		    currentSum = array[i] + array[left] + array[right]
		    if currentSum == targetSum:
			    triplets.append([array[i], array[left], array[right]])
			    left += 1
			    right -= 1
		    elif currentSum < targetSum:
			    left =+ 1
		    elif currentSum > targetSum:
			    right -= 1
    return triplets
	

threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
