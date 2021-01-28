#Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# Both similar approaches, one uses a for loop, one uses a while loop

#O(n) time, O(1) space
def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)

isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
 
#O(n) time, O(1) space
def isValidSubsequence(array, sequence):
	seqIdx = 0
	for value in array:
		if seqIdx == len(sequence) :
			break
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)

isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])