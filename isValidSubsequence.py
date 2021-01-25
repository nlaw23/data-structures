#Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.



#O(n) time, 0(1) space
def isValidSubsequence(array, sequence):
    arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)

isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])